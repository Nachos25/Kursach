import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { authApi } from "../lib/api";
import { setToken, getLocalUser } from "../lib/auth";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const navigate = useNavigate();

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    // Мок-логін: якщо є локальний користувач — звіряємо
    const u = getLocalUser();
    if (u && u.username === username && (!u.password || u.password === password)) {
      setToken("demo-token");
      navigate("/");
      return;
    }
    // Фолбек: дозволити admin/admin для швидкого входу
    if (username === "admin" && password === "admin") {
      setToken("demo-token");
      navigate("/");
      return;
    }
    // Остання спроба — бекенд
    try {
      const res = await authApi.login(username, password);
      setToken(res.access_token);
      navigate("/");
    } catch (e: any) {
      setError(e.message || "Помилка входу");
    }
  };

  return (
    <div className="rounded-2xl glass p-6 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Вхід</h1>
      <form onSubmit={submit} className="space-y-3">
        <input
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          type="text"
          placeholder="Логін"
          className="w-full rounded bg-neutral-900 border border-white/10 px-3 py-2"
          required
        />
        <input
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          type="password"
          placeholder="Пароль"
          className="w-full rounded bg-neutral-900 border border-white/10 px-3 py-2"
          required
        />
        {error && <div className="text-red-400 text-sm">{error}</div>}
        <button className="w-full px-4 py-2 rounded bg-brand-700 hover:bg-brand-600">Увійти</button>
        <div className="text-sm text-neutral-400">
          Немає акаунта? <Link className="text-brand-500" to="/register">Зареєструватись</Link>
        </div>
      </form>
    </div>
  );
}




