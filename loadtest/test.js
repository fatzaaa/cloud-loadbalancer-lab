import http from 'k6/http';
import { check } from 'k6';

export const options = {
  vus: 20,
  duration: '20s',
};

const BASE = __ENV.BASE_URL || 'http://localhost:8080';

export default function () {
  const res = http.get(`${BASE}/work`);
  check(res, { 'status 200': (r) => r.status === 200 });
}