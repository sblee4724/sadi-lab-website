import settings from '../data/settings.json';
import { L } from './util';
const show = settings.show as Record<string, boolean>;
export const NAV = [
  { key: 'research', href: '/research/', label: L('연구', 'Research') },
  { key: 'publications', href: '/publications/', label: L('논문', 'Publications') },
  { key: 'projects', href: '/projects/', label: L('과제', 'Projects') },
  { key: 'team', href: '/team/', label: L('팀', 'Team') },
  { key: 'news', href: '/news/', label: L('소식', 'News') },
  { key: 'gallery', href: '/gallery/', label: L('갤러리', 'Gallery') },
  { key: 'lecture', href: '/lecture/', label: L('강의', 'Lecture') },
].filter((n) => show[n.key] !== false);
export const showJoin = show.join !== false;
export const on = (k: string) => show[k] !== false;
