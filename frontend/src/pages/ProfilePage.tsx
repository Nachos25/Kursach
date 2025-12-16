import { useEffect, useState } from "react";
import { authApi } from "../lib/api";
import { getToken, getLocalUser } from "../lib/auth";
import { Link } from "react-router-dom";

export default function ProfilePage() {
  const token = getToken();
  const [data, setData] = useState<any | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!token) return;
    if (token === "demo-token") {
      const u = getLocalUser() || { username: "demo" };
      setData({ user: { username: u.username, full_name: u.fullName }, orders: [] });
      return;
    }
    authApi
      .me(token)
      .then(setData)
      .catch((e: any) => setError(e.message || "Помилка завантаження профілю"));
  }, [token]);

  if (!token)
    return (
      <div className="rounded-2xl glass p-6">
        Потрібно <Link className="text-brand-500" to="/login">увійти</Link>, щоб переглянути профіль.
      </div>
    );

  if (error) return <div className="rounded-2xl glass p-6 text-red-400">{error}</div>;
  if (!data) return <div className="rounded-2xl glass p-6">Завантаження...</div>;

  const { user, orders } = data;

  return (
    <div className="space-y-6">
      <div className="rounded-2xl glass p-6">
        <div className="text-sm text-neutral-400">Користувач</div>
        <div className="text-2xl font-bold">{user.full_name || user.username}</div>
        <div className="text-neutral-400">Логін: {user.username}</div>
      </div>

      <div className="rounded-2xl glass p-6">
        <h2 className="text-xl font-semibold mb-3">Мої замовлення</h2>
        {orders.length === 0 ? (
          <div className="text-neutral-400">Поки що немає замовлень.</div>
        ) : (
          <div className="space-y-3">
            {orders.map((o: any) => (
              <div key={o.id} className="rounded-lg bg-neutral-900 p-4">
                <div className="flex items-center justify-between">
                  <div className="font-medium">№ {o.id} — {o.status}</div>
                  <div>{o.total.toFixed(2)} $</div>
                </div>
                <div className="mt-2 text-sm text-neutral-300">
                  {o.items.map((it: any) => (
                    <div key={it.product_id} className="flex justify-between">
                      <span>Товар #{it.product_id}</span>
                      <span>x{it.quantity} · {it.unit_price.toFixed(2)} $</span>
                    </div>
                  ))}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}


