import random, json
random.seed(20261022)
BASE = 500
def pts(a):
    p = {}
    d=a['telecom_late']; p['V1 통신요금 연체(24개월)'] = 60 if d==0 else (20 if d<=2 else -40)
    m=a['autopay_months']; p['V2 공과금 자동이체 유지'] = 40 if m>=24 else (20 if m>=12 else 0)
    i=a['income']; p['V3 월 소득'] = 50 if i>=300 else (30 if i>=200 else 0)
    p['V4 고용 상태'] = {'정규직':40,'계약·프리랜서':10,'학생':0,'무직':-30}[a['employment']]
    p['V5 잔액 변동성'] = {'낮음':30,'중간':0,'높음':-30}[a['balance_vol']]
    l=a['loans']; p['V6 기존 대출 건수'] = 30 if l==0 else (0 if l==1 else -40)
    p['V7 거주 권역'] = {'A':30,'B':0,'C':-30}[a['region']]
    p['V8 스마트폰 등급'] = {'최신 플래그십':25,'중급':0,'구형':-25}[a['phone']]
    n=a['night_app']; p['V9 야간 앱 사용 비율'] = 15 if n<5 else (0 if n<=20 else -20)
    h=a['history_months']; p['V10 신용 이력 개월'] = 20 if h>=24 else (10 if h>=12 else 0)
    return p
MAXP={'V1 통신요금 연체(24개월)':60,'V2 공과금 자동이체 유지':40,'V3 월 소득':50,'V4 고용 상태':40,'V5 잔액 변동성':30,'V6 기존 대출 건수':30,'V7 거주 권역':30,'V8 스마트폰 등급':25,'V9 야간 앱 사용 비율':15,'V10 신용 이력 개월':20}
def decide(s): return "승인" if s>=620 else ("사람 검토" if s>=580 else "거절")
regions=['A']*10+['B']*10+['C']*10; random.shuffle(regions)
apps=[]
for k in range(30):
    r=regions[k]
    income=max(80,int(random.gauss({'A':290,'B':240,'C':190}[r],60)//10*10))
    emp=random.choices(['정규직','계약·프리랜서','학생','무직'],[45,25,20,10])[0]
    if emp=='학생': income=min(income,150)
    if emp=='무직': income=min(income,80)
    phone=random.choices(['최신 플래그십','중급','구형'],{'A':[55,35,10],'B':[30,45,25],'C':[15,40,45]}[r])[0]
    night=random.choice([2,3,4,8,12,15,18,25,30,35]) if emp!='정규직' else random.choice([2,3,4,6,10,14,22])
    age=random.randint(19,34)
    apps.append(dict(id=f'A{k+1:02d}',age=age,age_band='19-24' if age<=24 else ('25-29' if age<=29 else '30-34'),
      gender=random.choice(['여','남']),region=r,income=income,employment=emp,
      telecom_late=random.choices([0,1,2,3,5],[50,20,12,10,8])[0],
      autopay_months=random.choice([3,6,10,14,18,24,30,36]),
      balance_vol=random.choices(['낮음','중간','높음'],[35,40,25])[0],
      loans=random.choices([0,1,2],[55,30,15])[0],phone=phone,night_app=night,
      history_months=random.choice([0,4,8,12,16,20,26,36])))
rows=[]
for a in apps:
    p=pts(a); s=BASE+sum(p.values()); d=decide(s)
    gaps=sorted(((MAXP[k]-v,k) for k,v in p.items()),reverse=True)
    reasons='-' if d=='승인' else ' / '.join(f'{k} ({p[k]:+d}, 최고점 대비 -{g})' for g,k in gaps[:2])
    rows.append(dict(a,score=s,decision=d,reasons=reasons,points=p))
json.dump(rows,open('rows.json','w'),ensure_ascii=False,indent=1)
for key in ['region','age_band','gender','employment']:
    print(key)
    for g in sorted(set(r[key] for r in rows)):
        sub=[r for r in rows if r[key]==g]; n=len(sub)
        c=[sum(r['decision']==x for r in sub) for x in ['승인','사람 검토','거절']]
        print(f'  {g}: n={n} 승인 {c[0]} ({c[0]/n:.0%}) 검토 {c[1]} 거절 {c[2]}')
for r in rows: print(r['id'],r['region'],r['income'],r['employment'],r['phone'],r['night_app'],r['score'],r['decision'],r['reasons'])
