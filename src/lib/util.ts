// Small helpers shared by all pages.
export type Bi = { ko: string; en: string };

const esc = (s: string) =>
  String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

/** plain text from the CMS -> safe HTML: **bold** becomes highlighted, new lines become <br> */
export const rich = (s: string) =>
  esc(s).replace(/\*\*(.+?)\*\*/g, '<b class="hl">$1</b>').replace(/\n/g, '<br>');

/** bilingual value -> both languages in the markup (CSS shows one) */
export const bi = (v: Bi | string | undefined) => {
  if (v == null) return '';
  if (typeof v === 'string') return rich(v);
  if ((v.en ?? '') === '' || v.en === v.ko) return rich(v.ko);
  return `<span class="ko">${rich(v.ko)}</span><span class="en">${rich(v.en)}</span>`;
};

export const L = (ko: string, en: string): Bi => ({ ko, en });
export const RV = ['rv', 'rv2', 'rv3', 'rv4'];
export const pad2 = (n: number) => String(n).padStart(2, '0');

export const hexToRgb = (h: string) => {
  const m = h.replace('#', '');
  const n = parseInt(m.length === 3 ? m.split('').map((c) => c + c).join('') : m, 16);
  return `${(n >> 16) & 255} ${(n >> 8) & 255} ${n & 255}`;
};

export const AREA_COLOR: Record<string, string> = { comp: 'var(--a1)', intel: 'var(--a2)', equip: 'var(--a3)' };
export const AREA_LABEL: Record<string, Bi> = {
  comp: L('전산역학', 'Comp. Mechanics'),
  intel: L('지능형구조', 'Intelligent Structures'),
  equip: L('첨단기기개발', 'Equipment'),
};
