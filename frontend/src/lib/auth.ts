const TOKEN_KEY = "techstore_token";
const USER_KEY = "perforator_user";

export function getToken(): string | null {
  return localStorage.getItem(TOKEN_KEY);
}

export function setToken(token: string) {
  localStorage.setItem(TOKEN_KEY, token);
}

export function logout() {
  localStorage.removeItem(TOKEN_KEY);
  localStorage.removeItem(USER_KEY);
}

export type LocalUser = { username: string; fullName?: string; password?: string };

export function getLocalUser(): LocalUser | null {
  try {
    const raw = localStorage.getItem(USER_KEY);
    return raw ? (JSON.parse(raw) as LocalUser) : null;
  } catch {
    return null;
  }
}

export function setLocalUser(u: LocalUser) {
  localStorage.setItem(USER_KEY, JSON.stringify(u));
}




