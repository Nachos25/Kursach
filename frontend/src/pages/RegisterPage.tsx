import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { authApi } from "../lib/api";
import { setToken, setLocalUser } from "../lib/auth";

export default function RegisterPage() {
  const [username, setUsername] = useState("");
  const [fullName, setFullName] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [ok, setOk] = useState(false);
  const navigate = useNavigate();

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    // Мок-реєстрація: запис локально + миттєва авторизація
    if (!username || !password) {
      setError("Вкажіть логін та пароль");
      return;
    }
    setLocalUser({ username, fullName, password });
    setToken("demo-token");
    navigate("/");
  };

  return (
    <div className="rounded-2xl glass p-6 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Реєстрація</h1>
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
          value={fullName}
          onChange={(e) => setFullName(e.target.value)}
          type="text"
          placeholder="Повне ім'я (необов'язково)"
          className="w-full rounded bg-neutral-900 border border-white/10 px-3 py-2"
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
        {ok && <div className="text-green-400 text-sm">Успішно! Перехід до входу...</div>}
        <button className="w-full px-4 py-2 rounded bg-brand-700 hover:bg-brand-600">Зареєструватись</button>
        <div className="text-sm text-neutral-400">
          Вже маєте акаунт? <Link className="text-brand-500" to="/login">Увійти</Link>
        </div>
      </form>
    </div>
  );
}




