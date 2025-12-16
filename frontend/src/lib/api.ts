export const API_BASE: string = (import.meta as any).env?.VITE_API_URL || "http://127.0.0.1:8000/api";

async function request<T>(path: string, options: RequestInit = {}): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
    ...options,
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || `HTTP ${res.status}`);
  }
  return res.json();
}

export const api = {
  get: <T = any>(path: string) => request<T>(path),
  post: <T = any>(path: string, body?: unknown, token?: string) =>
    request<T>(path, {
      method: "POST",
      body: body ? JSON.stringify(body) : undefined,
      headers: token ? { Authorization: `Bearer ${token}` } : undefined,
    }),
};

export const authApi = {
  login: async (username: string, password: string) => {
    const form = new URLSearchParams();
    form.set("username", username);
    form.set("password", password);
    const res = await fetch(`${API_BASE.replace(/\/api$/, "")}/api/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: form.toString(),
    });
    if (!res.ok) throw new Error(await res.text());
    return res.json() as Promise<{ access_token: string }>;
  },
  register: (payload: { username: string; password: string; full_name?: string; email?: string }) =>
    request("/auth/register", { method: "POST", body: JSON.stringify(payload) }),
  orders: (token: string) => request("/orders", { headers: { Authorization: `Bearer ${token}` } } as any),
  me: (token: string) => request("/auth/me", { headers: { Authorization: `Bearer ${token}` } } as any),
  instant: async (payload: { username: string; password?: string; full_name?: string }) => {
    const params = new URLSearchParams();
    params.set("username", payload.username);
    if (payload.password) params.set("password", payload.password);
    if (payload.full_name) params.set("full_name", payload.full_name);
    return request(`/auth/instant?${params.toString()}`, { method: "POST" });
  },
};




