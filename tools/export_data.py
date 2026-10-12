# One-off: write the v5 design content into editable JSON files (src/data/*.json)
import json, os
O="OOOOOOOOO"
D=os.path.join(os.path.dirname(__file__),"..","src","data")
def L(ko,en=None): return {"ko":ko,"en":en if en is not None else ko}
def w(name,obj):
    json.dump(obj,open(os.path.join(D,name+".json"),"w"),ensure_ascii=False,indent=2)

w("settings",{
 "lab":{"short":"SADI","name":L("구조해석·설계·지능 연구실","Structural Analysis, Design & Intelligence Lab"),
        "full":"Structural Analysis, Design & Intelligence Laboratory",
        "dept":L("부산대학교 공과대학 기계공학부","School of Mechanical Engineering, College of Engineering, Pusan National University"),
        "univ":L("부산대학교","Pusan National University")},
 "contact":{"email":"sb.lee@pusan.ac.kr","tel":L("051-510-2497","+82-51-510-2497"),
        "room":L("부산대학교 기계관 619호","PNU Mechanical Engineering Bldg. Room 619"),
        "address":L("부산광역시 금정구 부산대학로63번길 2, 부산대학교 기계관 619호","Room 619, Mechanical Engineering Bldg., Pusan National University, 2 Busandaehak-ro 63beon-gil, Geumjeong-gu, Busan 46241, Korea"),
        "googleMap":"https://maps.app.goo.gl/QmCCBTvf3ERLgCiXA","naverMap":"https://naver.me/F9N44XkL"},
 "hero":{"imageLight":"/images/hero-light.webp","imageDark":"/images/hero-dark.webp","position":"70% 50%",
        "eyebrow":L("부산대학교 공과대학 기계공학부","School of Mechanical Engineering · Pusan National University"),
        "lead":L("구조물을 계산으로 해석하고(Analysis), 계측과 모델로 상태를 읽어내며(Intelligence), 더 안전한 기기를 설계합니다(Design).\n**전산역학**, **지능형구조**, **첨단기기개발**을 연구합니다.",
                 "We analyze structures by computation, read their state with measurements and models, and design safer equipment.\nOur research: **computational mechanics**, **intelligent structures** and **advanced equipment development**.")},
 "show":{"popup":True,"recruitBox":True,"partners":True,"research":True,"publications":True,"projects":True,"team":True,"news":True,"gallery":True,"lecture":True,"join":True},
 "popup":{"title":L("대학원생 · 박사후연구원 · 학부연구생 모집","Recruiting graduate students, postdocs & undergraduate researchers"),
        "body":L("부산대학교 기계공학부 구조해석·설계·지능 연구실(SADI)에서 **더 안전하고 가치 있는 엔지니어링**을 위한 구조 연구에 함께할 신입 대학원생(석사·박사), 박사후연구원 및 학부연구생을 모집합니다.",
                 "The Structural Analysis, Design & Intelligence Lab (SADI) at PNU Mechanical Engineering is recruiting new M.S./Ph.D. students, postdoctoral researchers and undergraduate researchers to work toward **safer, more valuable engineering**."),
        "points":[L("전산역학(유한요소·멀티피직스 해석), 지능형구조(가상측정·디지털 트윈), 첨단기기개발(차세대 원자로 기기 설계) 등 다양한 연구 분야","Computational mechanics (finite elements, multiphysics), intelligent structures (virtual sensing, digital twins) and advanced equipment development (next-generation reactor components)"),
                  L("국내외 학술대회 발표, 연구기관·산업체 공동연구 참여 등 함께 성장하는 연구 환경","Conference presentations at home and abroad and joint research with institutes and industry")],
        "closing":L("연구실에 관심 있는 학생은 메일로 연락 바랍니다.","If you are interested, please get in touch by email."),
        "signature":L("이승보 교수","Prof. Sungbo Lee")},
 "recruit":{"title":L("함께 연구할 사람을 찾습니다","We are looking for people to research with"),
        "body":L("석사·박사과정 학생, 학부연구생, 박사후연구원을 모집합니다. 구조해석, 가상측정, 기기 설계에 관심이 있다면 이메일로 연락해 주세요.","We are recruiting M.S. and Ph.D. students, undergraduate researchers and postdocs. If structural analysis, virtual sensing or equipment design interests you, send us an email.")},
 "theme":{"default":"light",
   "light":{"bg":"#F7F6F3","surface":"#FFFFFF","surface2":"#ECE9E3","line":"#E4E1DB","line2":"#CFCAC2","text":"#16130F","text2":"#57534E","text3":"#766F69","accent":"#2F5BD3","area1":"#2F5BD3","area2":"#0E9384","area3":"#D9601A"},
   "dark":{"bg":"#0C0A09","surface":"#141210","surface2":"#1C1917","line":"#292524","line2":"#3A3532","text":"#FAFAF9","text2":"#A8A29E","text3":"#8A837E","accent":"#5B8CFF","area1":"#5B8CFF","area2":"#2DD4BF","area3":"#FB923C"}},
 "fonts":{"display":"Space Grotesk","body":"Noto Sans KR","mono":"JetBrains Mono"}
})

AREAS=[
 dict(key="comp",num="01",title=L("전산역학","Computational Mechanics"),sub="Finite Elements & Multiphysics",image="/images/area1-shell.webp",imagePos="50% 40%",
  summary=L("유한요소 정식화와 멀티피직스 연성해석으로 구조·열·충격 거동을 정확하고 빠르게 예측합니다.","We predict structural, thermal and impact behavior accurately and fast with finite element formulations and coupled multiphysics analysis."),
  headline=L("정확하고, 빠르고, 믿을 수 있는 해석","Accurate, fast and trustworthy analysis"),
  intro=L("복잡한 형상과 비선형 재료, 열·유동·충격이 얽힌 문제에서 해석의 신뢰도는 요소 정식화와 모델링 선택에 달려 있습니다.\nSADI는 새로운 유한요소를 개발하고, 연성해석과 축소모델로 해석의 정확도와 속도를 함께 끌어올립니다.","For complex geometries, nonlinear materials and coupled thermal, flow and impact problems, the reliability of analysis depends on element formulation and modeling choices.\nSADI develops new finite elements and raises both accuracy and speed with coupled analysis and reduced-order models."),
  steps=[dict(title=L("물리 모델링","Physics modeling"),text=L("구조·열·유동·재료 거동을 지배방정식으로 정식화합니다.","Formulate structural, thermal, flow and material behavior as governing equations.")),
         dict(title=L("요소 정식화","Element formulation"),text=L("다각형·적층 쉘 등 새로운 유한요소로 이산화합니다.","Discretize with new elements such as polygonal and layered shell elements.")),
         dict(title=L("연성 해석","Coupled solution"),text=L("열-구조, 유체-구조, 충격 해석을 수행합니다.","Solve thermo-mechanical, fluid–structure and impact problems.")),
         dict(title=L("검증·축소","Validation & ROM"),text=L("실험과 비교하고 축소모델로 빠르게 만듭니다.","Validate against experiments and accelerate with reduced-order models."))],
  activities=[dict(title=L("다각형 유한요소와 기하 비선형 해석","Polygonal finite elements for geometric nonlinearity"),ref="Strain-smoothed polygonal element · Computers & Structures (in preparation)"),
              dict(title=L("미끄럼이 있는 적층 쉘 요소의 동적 거동","Layered shell elements with interlayer slip"),ref="Steel and Composite Structures 60(1) (2026)"),
              dict(title=L("유탄성 해석에서 응력 RAO 직접 계산","Direct stress RAOs in hydroelastic analysis"),ref="Ocean Engineering 312 (2024)"),
              dict(title=L("초고변형률속도 재료 모델과 충격 해석","High strain-rate material models and impact analysis"),ref="Int. J. Impact Engineering 149 (2021), 180 (2023) · Metals 12(3) (2022)")]),
 dict(key="intel",num="02",title=L("지능형구조","Intelligent Structures"),sub="Virtual Sensing & Digital Twin",image="/images/area2-virtual-sensing.webp",imagePos="72% 50%",
  summary=L("소수의 센서와 계산모델을 결합한 가상측정으로 구조물 전체의 변형과 상태를 실시간으로 추정합니다.","We estimate the full-field deformation and state of structures in real time by fusing a few sensors with computational models."),
  headline=L("소수의 센서로 구조 전체를 읽어내다","Reading a whole structure from a few sensors"),
  intro=L("실제 구조물에는 몇 개의 센서만 붙일 수 있지만, 안전 판단에 필요한 것은 구조 전체의 변형과 응력입니다.\n가상측정은 계측 신호와 계산모델의 모드 정보를 결합해 센서가 없는 위치까지 응답을 실시간으로 재구성합니다.","Only a few sensors can be installed on a real structure, yet safety decisions need the full-field deformation and stress.\nVirtual sensing fuses measured signals with modal information from the computational model to reconstruct responses in real time — even where there are no sensors."),
  steps=[dict(title=L("희소 계측","Sparse measurement"),text=L("가속도·변형률 등 소수의 센서 신호를 받습니다.","Acquire a few acceleration and strain signals.")),
         dict(title=L("모델 기반 추론","Model-based inference"),text=L("모드 중첩과 정규화로 전체 응답을 추정합니다.","Estimate the full response by mode superposition and regularization.")),
         dict(title=L("상태 재구성","State reconstruction"),text=L("변형·응력장과 손상 지표, 잔여수명을 산출합니다.","Produce deformation and stress fields, damage indicators and remaining life."))],
  table=dict(head=[L("항목","Item"),L("기존 계측","Conventional sensing"),L("가상측정","Virtual sensing")],
             rows=[[L("측정 범위","Coverage"),L("센서 위치의 점 정보","Point values at sensors"),L("구조 전체의 연속 필드","Continuous full field")],
                   [L("필요 센서 수","Sensors needed"),L("많음","Many"),L("소수 (최적 배치)","Few (optimally placed)")],
                   [L("접근 불가 부위","Inaccessible regions"),L("측정 불가","Not measurable"),L("모델로 추정","Estimated by model")],
                   [L("실시간성","Real time"),L("가능","Yes"),L("가능 (경량 연산)","Yes (lightweight)")],
                   [L("디지털 트윈 연계","Digital-twin link"),L("제한적","Limited"),L("직접 연계","Direct")]]),
  activities=[dict(title=L("실험 규모 자켓 구조물의 실시간 변형률장 추정","Real-time strain-field estimation on a lab-scale jacket"),ref="Computers & Structures 298 (2024)"),
              dict(title=L("운용하중을 고려한 변형률 센서 배치","Strain sensor placement under operational loads"),ref="Computers & Structures 315 (2025)"),
              dict(title=L("가상측정을 위한 적응형 정규화","Adaptive regularization for virtual sensing"),ref="Ocean Engineering 354 (2026)"),
              dict(title=L("BWB 항공기 구조의 전역 변형률 재구성","Full-field strain reconstruction of BWB aircraft"),ref="Structural Engineering and Mechanics 98(1) (2026)")]),
 dict(key="equip",num="03",title=L("첨단기기개발","Advanced Equipment Development"),sub="Design & Integrity for Extreme Environments",image="/images/area3-equipment.webp",imagePos="50% 45%",
  summary=L("원자로·고온·극한환경 기기의 설계와 건전성 평가로 차세대 첨단기기를 개발합니다.","We develop next-generation equipment through design and integrity assessment for reactor, high-temperature and extreme environments."),
  headline=L("극한환경에서도 견디는 기기를 설계하다","Designing equipment that endures extreme environments"),
  intro=L("소형모듈원자로(SMR)와 같은 차세대 원자로와 에너지 시스템의 기기는 고온, 부식성 용융염을 견뎌야 합니다.\nSADI는 해석과 건전성 평가를 설계 단계에 통합해 새로운 기기를 개발합니다.","Equipment for next-generation reactors and energy systems such as small modular reactors (SMR) must withstand high temperatures and corrosive molten salts.\nSADI integrates analysis and integrity assessment into the design stage to develop new equipment."),
  steps=[dict(title=L("요구조건 정의","Requirements"),text=L("운전 온도·하중·수명 등 설계 조건을 정합니다.","Set operating temperature, loads and design life.")),
         dict(title=L("해석 기반 설계","Analysis-driven design"),text=L("열·구조 연성해석으로 형상과 재료를 결정합니다.","Decide geometry and materials with thermo-structural analysis.")),
         dict(title=L("건전성 평가","Integrity assessment"),text=L("크리프·피로·파손 기준으로 평가합니다.","Assess against creep, fatigue and failure criteria.")),
         dict(title=L("시험·개선","Testing & iteration"),text=L("시험 결과로 설계를 개선합니다.","Refine the design with test results."))],
  activities=[dict(title=L("용융염원자로(MSR) 동결밸브의 열적 거동 해석","Thermal behavior of freeze valves for molten salt reactors"),ref="한국원자력학회 (2025) · "+O),
              dict(title=L("용융염 환경 레이저 클래딩 소재의 부식·기계적 특성","Corrosion and mechanical properties of laser-cladded alloys in molten salt"),ref="Nuclear Engineering and Technology (in preparation)"),
              dict(title=L("원자력 시설 내부 폭발 하중의 TNT 등가성 평가","TNT equivalency of internal explosions in nuclear facilities"),ref="Structural Engineering and Mechanics 97(3) (2026)"),
              dict(title=L("고온 기기 구조 설계 및 건전성 평가",O),ref=O)])]
w("research",{
 "hero":dict(title=L("구조의 전 생애를\n계산으로 다룹니다","Handling the whole life of a structure\nby computation"),lead=L("해석으로 거동을 예측하고, 계측과 모델로 현재 상태를 읽어내며, 그 이해를 새로운 기기 설계로 연결합니다.","We predict behavior by analysis, read the present state with measurements and models, and carry that understanding into new equipment design."),image="/images/research-overview.webp"),
 "homeTitle":L("구조물을 계산하고, 읽어내고, 만들어내는\n모든 과정을 연구합니다","We study every step — computing, reading\nand building structures"),
 "overview":dict(title=L("구조물은 말하지 않습니다","Structures do not speak"),paragraphs=[
   L("원자로 기기, 해양 구조물, 항공기처럼 극한 조건에서 운용되는 구조물은 내부의 응력과 손상을 직접 보여 주지 않습니다. 센서를 붙일 수 있는 위치는 제한되고, 설계 단계의 해석은 실제 운용 조건과 어긋나기 쉽습니다.","Structures operating in extreme conditions — reactor components, offshore structures, aircraft — do not reveal their internal stress and damage. Sensor locations are limited, and design-stage analysis easily drifts from real operating conditions."),
   L("SADI는 이 간극을 계산으로 메웁니다. 정확한 전산해석으로 거동을 예측하고, 소수의 계측으로 구조 전체의 상태를 추정하며, 그 결과를 더 안전한 첨단기기 설계로 되돌립니다.","SADI closes this gap by computation: we predict behavior with accurate analysis, estimate the whole structural state from a few measurements, and feed the results back into safer advanced equipment design.")]),
 "areas":AREAS,
 "methods":[dict(title=L("해석 도구","Computational tools"),items=[dict(label="FE Analysis",value="ABAQUS · ANSYS · LS-DYNA · ADINA"),dict(label="Pre-processing / CAD",value="HyperMesh · CATIA · Inventor"),dict(label="Programming",value="Python · MATLAB · Fortran"),dict(label="Machine learning",value="TensorFlow · Keras")]),
            dict(title=L("실험 및 계측","Experiments & measurement"),items=[dict(label="Material testing",value="UTM · SHPB · Taylor impact"),dict(label="Full-field measurement",value="DIC"),dict(label="Structural sensing",value="Strain · Acceleration · Displacement"),dict(label="Data acquisition",value="LabVIEW")])]
})
w("partners",{"home":[dict(name="KAIST",desc=L("한국과학기술원","Korea Advanced Institute of Science & Technology")),dict(name="KAERI",desc=L("한국원자력연구원","Korea Atomic Energy Research Institute"))]+[dict(name=O,desc=L("협력 기관","Partner"))]*4,
 "groups":[dict(title=L("연구기관","Research institutes"),items=[L("한국원자력연구원 (KAERI)","Korea Atomic Energy Research Institute (KAERI)"),L(O)]),
           dict(title=L("국내 대학","Universities"),items=[L("한국과학기술원 (KAIST)","KAIST"),L(O)]),
           dict(title=L("해외 대학","International"),items=[L(O)]),
           dict(title=L("산업체","Industry"),items=[L(O),L(O)])]})
P=lambda kind,area,y,pre,me,post,t,j,v,link="",featured=False: dict(kind=kind,area=area,year=y,authorsBefore=pre,me=me,authorsAfter=post,title=t,journal=j,volume=v,link=link,featured=featured)
w("publications",{"journals":[
 P("international","intel",2026,"","Lee S",", Park S, Kim G","Adaptive regularization for virtual sensing of structural deformation","Ocean Engineering","354 (2026) 125030",featured=True),
 P("international","comp",2026,"","Lee S",", Park S","The modal behavior of the layered shell element with interlayer slips","Steel and Composite Structures","60(1) (2026) 167–187"),
 P("international","intel",2026,"Shin MC, ","Lee S",", Cho SP","Full-field strain reconstruction of BWB aircraft structures using mode superposition-based virtual sensing","Structural Engineering and Mechanics","98(1) (2026) 77"),
 P("international","equip",2026,"Lee SG, ","Lee S",", Lee PS","TNT equivalency of MegaMEX and CONWEP-based modeling of fully vented internal explosions in nuclear facilities","Structural Engineering and Mechanics","97(3) (2026) 393"),
 P("international","intel",2025,"","Lee S",", Lee PS","Strain sensor placement method considering operational loads for virtual sensing of structural deformation","Computers & Structures","315 (2025) 107763",featured=True),
 P("international","intel",2024,"","Lee S",", Park M, Oh M-H, Lee P-S","Virtual sensing for real-time strain field estimation and its verification on a laboratory-scale jacket structure under water waves","Computers & Structures","298 (2024) 107344","https://www.sciencedirect.com/science/article/abs/pii/S0045794924000737",featured=True),
 P("international","comp",2024,"Park M, ","Lee S",", Kim K-T, Lee P-S","Direct calculation of stress RAOs in hydroelastic analysis","Ocean Engineering","312 (2024) 118894","https://www.sciencedirect.com/science/article/abs/pii/S0029801824022327"),
 P("international","comp",2023,"Noh D, Fazily P, Yu K, ","Lee S",", Ko DK, Sung MJ, Huh H, Yoon JW","Tungsten alloy impact fracture for frangible armor piercing","International Journal of Impact Engineering","180 (2023) 104681","https://www.sciencedirect.com/science/article/abs/pii/S0734743X23001926"),
 P("international","comp",2022,"","Lee S",", Yu K, Huh H, Kolman R, Arnoult X","Dynamic hardening of AISI 304 steel at a wide range of strain rates and its application to shot peening simulation","Metals","12(3) (2022) 403","https://doi.org/10.3390/met12030403"),
 P("international","comp",2021,"","Lee S",", Huh H","Shear stress hardening curves of AISI 4130 steel at ultra-high strain rates with Taylor impact tests","International Journal of Impact Engineering","149 (2021) 103789","https://www.sciencedirect.com/science/article/abs/pii/S0734743X20308599"),
 P("domestic","comp",2021,"노동환, 유광현, ","이승보",", 고동균, 성민제, 허훈, 윤정환","Mohr–Coulomb 파단모델을 이용한 텅스텐 합금의 충격 파단 예측","소성가공학회지","30 (2021) 16–21")],
 "conferences":[dict(year=y,title=t,venue=c) for y,t,c in [("2025","Numerical evaluation of thermal behavior of freeze valve system for K-MSR","한국원자력학회 / Korean Nuclear Society"),("2024","모드 기반 실시간 변형 추정","한국전산구조공학회 / COSEIK"),("2023","Performance evaluation of three sensor placement methods","ASEM23"),("2023","적합직교분해 기저를 이용한 자켓 구조물의 변형","대한조선학회 / SNAK"),("2022","Automation of frequency domain decomposition for operational modal analysis using finite element model","Computational Structures Technology (CST)"),("2018","Prediction of shear properties at ultra-high strain rates","AEPA")]]})
w("projects",{"projects":[dict(status="ongoing",period="2026–"+O,title=L(O+" (과제명)",O+" (Project title)"),funder=O+" · 주관/참여")]*2+[dict(status="ongoing",period="2026–"+O,title=L(O+" (과제명)",O+" (Project title)"),funder=O)]+[dict(status="done",period="20OO–20OO",title=L(O+" (과제명)",O+" (Project title)"),funder=O)]*2,
 "patents":[dict(title=O+" (특허명)",status="filed",number=O,date="20OO.OO.OO"),dict(title=O+" (특허명)",status="granted",number=O,date="20OO.OO.OO")]})
w("team",{"pi":dict(name=L("이승보","Sungbo Lee"),degree="Ph.D.",photo="/images/prof-sungbo-lee.jpg",position=L("부산대학교 기계공학부 조교수","Assistant Professor, School of Mechanical Engineering, Pusan National University"),
   short=L("前 한국원자력연구원 선임연구원 · KAIST 기계공학 박사","Former Senior Researcher, KAERI · Ph.D., Mechanical Engineering, KAIST"),
   links=[dict(label="Google Scholar",url="#"),dict(label="ORCID",url="#"),dict(label="ResearchGate",url="#")],
   career=[dict(period="2026.09 –",text=L("부산대학교 기계공학부 조교수","Assistant Professor, School of Mechanical Engineering, Pusan National University")),
           dict(period="2024.08 – 2026.08",text=L("한국원자력연구원 선임연구원 (차세대원자로기술개발부)","Senior Researcher, KAERI (Gen-IV Reactor Technology Development Division)")),
           dict(period="2019 – 2024",text=L("KAIST 기계공학 박사","Ph.D., Mechanical Engineering, KAIST")),
           dict(period="2017 – 2019",text=L("KAIST 기계공학 석사","M.S., Mechanical Engineering, KAIST")),
           dict(period="2011 – 2017",text=L("부산대학교 기계공학부 학사","B.S., Mechanical Engineering, Pusan National University"))],
   honors=[dict(period="2011 – 2016",text=L("대통령과학장학금","Presidential Science Scholarship")),dict(period=O,text=L(O))]),
 "members":[], "alumni":[],
 "openings":[L("박사과정 · 모집 중","Ph.D. student · open"),L("석사과정 · 모집 중","M.S. student · open"),L("박사후연구원 · 모집 중","Postdoc · open"),L("학부연구생 · 모집 중","Undergraduate · open")]})
N=lambda date,cat,title,summary,image="": dict(date=date,category=cat,title=title,summary=summary,image=image)
w("news",{"items":[
 N("2026-09-01","people",L("이승보 교수, 부산대학교 기계공학부 조교수 부임","Prof. Sungbo Lee joins the School of Mechanical Engineering, Pusan National University"),L("SADI Lab이 부산대학교에서 연구를 시작합니다.","SADI Lab begins its research at Pusan National University."),"/images/prof-sungbo-lee.jpg"),
 N("2026-09-02","recruit",L("2027학년도 전기 대학원생 모집","Graduate student recruitment for Spring 2027"),L("석사·박사과정, 박사후연구원 및 학부연구생을 모집합니다. 자격·지원 방법: "+O,"M.S./Ph.D. students, postdocs and undergraduate researchers wanted. Details: "+O),"/images/hero-dark.webp"),
 N("2026-03-01","paper",L("Ocean Engineering 논문 게재","Paper published in Ocean Engineering"),L("Adaptive regularization for virtual sensing of structural deformation"),"/images/news-bwb.webp"),
 N("2026-02-01","paper",L("Steel and Composite Structures 논문 게재","Paper published in Steel and Composite Structures"),L("The modal behavior of the layered shell element with interlayer slips"),"/images/news-layer.webp"),
 N("2025-06-01","paper",L("Computers & Structures 논문 게재","Paper published in Computers & Structures"),L("Strain sensor placement method considering operational loads for virtual sensing of structural deformation"),"/images/news-jacket.webp")]})
w("gallery",{"items":[dict(caption=L(O),date="2026. OO.",image="")]*6})
w("lectures",{"intro":L("부산대학교 기계공학부에서 담당하고 있는 강의입니다.","Courses taught at the School of Mechanical Engineering, Pusan National University."),"courses":[
 dict(title=L("동역학","Dynamics"),level=L("학부","Undergraduate"),semester=O,description=L("뉴턴 역학을 바탕으로 질점과 강체의 운동을 해석합니다. 운동학, 힘과 가속도, 일과 에너지, 충격량과 운동량을 다룹니다.","Motion of particles and rigid bodies based on Newtonian mechanics — kinematics, force and acceleration, work and energy, impulse and momentum.")),
 dict(title=L("유한요소법","Finite Element Method"),level=L("학부 · 대학원","Undergraduate · Graduate"),semester=O,description=L("변분 원리와 약형식에서 출발해 유한요소를 정식화하고, 직접 코드로 구현해 구조 문제를 풉니다.","From variational principles and weak forms to element formulation, with hands-on implementation for structural problems."))]})
w("join",{"headline":L("정답을 외우는 사람보다\n구조가 왜 그렇게 움직이는지\n끝까지 묻는 사람","Not the one who memorizes answers,\nbut the one who keeps asking\nwhy a structure moves as it does"),"image":"/images/equipment.webp",
 "qualities":[dict(title=L("질문하는 힘","Asking questions"),text=L("결과보다 이유를 먼저 궁금해하고, 해석 결과를 그대로 믿지 않고 다시 확인합니다.","You wonder why before what, and you verify analysis results instead of trusting them blindly.")),
              dict(title=L("끝까지 붙잡는 끈기","Persistence"),text=L("수렴하지 않는 해석과 맞지 않는 실험 앞에서 원인을 찾을 때까지 버팁니다.","You stay with a non-converging model or a mismatched test until you find the cause.")),
              dict(title=L("깊이 몰입하는 태도","Deep focus"),text=L("한 문제를 오래 들여다보고, 그 과정에서 배운 것을 동료와 나눕니다.","You look at one problem for a long time and share what you learn with your colleagues."))],
 "documents":[L("이력서 (CV)","Curriculum vitae"),L("성적증명서","Academic transcript"),L("관심 연구 주제 한 단락","A paragraph on the research you want to do")]})
print("ok")
