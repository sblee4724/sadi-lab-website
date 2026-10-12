# SADI Lab 홈페이지

부산대학교 기계공학부 구조해석·설계·지능 연구실(SADI) 홈페이지입니다.
Astro로 만든 정적 사이트이고, `/admin` 관리자 페이지(Decap CMS)에서 내용을 고칩니다.

## 구조

| 위치 | 내용 |
|---|---|
| `src/data/*.json` | 모든 글·목록 (관리자 페이지가 이 파일을 고칩니다) |
| `src/data/settings.json` | on/off 스위치, 홈 배경 이미지, 색상, 글꼴, 연락처, 팝업 |
| `src/pages/` | 페이지 9개 (홈, 연구, 논문, 과제, 팀, 소식, 갤러리, 강의, 모집) |
| `src/components/` | 머리글, 바닥글, 트러스 A 로고, 팝업 등 |
| `src/styles/global.css` | 레이아웃·반응형(모바일) 스타일 |
| `public/images/` | 이미지 (관리자에서 올린 파일은 `public/images/uploads/`) |
| `public/admin/` | 관리자 페이지 |
| `tools/cms-config.src.yml` | 관리자 화면 구성 원본 → `npm run cms-config`로 `public/admin/config.yml` 생성 |

## 처음 올리기 (한 번만)

1. **GitHub**: 계정을 만들고 새 저장소(예: `sadi-lab-website`)를 만든 뒤 이 폴더를 올립니다.
2. **관리자 연결**: `sblee4724/sadi-lab-website` 저장소로 이미 설정되어 있습니다. 저장소 이름을 바꾸면 `tools/cms-config.src.yml`의 `repo`도 바꾸고 `npm run cms-config`를 실행하세요.
3. **Netlify**: netlify.com에 GitHub 계정으로 가입 → *Add new site → Import from GitHub* → 저장소 선택 → 그대로 *Deploy*. (`netlify.toml`에 빌드 설정이 들어 있습니다.)
4. **관리자 로그인 허용**: GitHub *Settings → Developer settings → OAuth Apps → New* 에서
   - Homepage URL: `https://<사이트주소>`
   - Callback URL: `https://api.netlify.com/auth/done`
   만든 뒤 Client ID/Secret을 Netlify *Site configuration → Access & security → OAuth → Install provider (GitHub)* 에 넣습니다.
5. `https://<사이트주소>/admin/` 에서 GitHub로 로그인하면 됩니다.

## 내용 고치기

- 관리자 페이지에서 고치고 **게시**를 누르면 GitHub에 저장되고, Netlify가 1분 안팎으로 사이트를 다시 만듭니다.
- 한국어/영어 칸이 나뉘어 있습니다. 영어를 비워 두면 영어 화면에도 한국어가 나옵니다.
- 문단 칸에서는 줄바꿈이 그대로 반영되고, `**이렇게**` 쓰면 강조됩니다.

## 도메인

- 구입한 도메인: Netlify *Domain management → Add a domain* 에서 연결합니다.
- 학교 도메인(예: `sadi.pusan.ac.kr`): 학교 전산 담당에 **CNAME → `<사이트이름>.netlify.app`** 등록을 요청한 뒤 Netlify에 같은 주소를 추가합니다. HTTPS 인증서는 자동으로 발급됩니다.
- 도메인이 정해지면 `astro.config.mjs`의 `site` 값을 바꿔 주세요.

## 내 컴퓨터에서 미리 보기 (선택)

```bash
npm install
npm run dev          # http://localhost:4321
npm run cms          # 다른 창에서 실행하면 http://localhost:4321/admin/index.html 에서 로그인 없이 편집
```
