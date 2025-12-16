import { useEffect, useState } from "react";
import { authApi } from "../lib/api";
import { getToken } from "../lib/auth";
import { Link } from "react-router-dom";

export default function OrdersPage() {
  const token = getToken();
  const [orders, setOrders] = useState<any[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!token) return;
    if (token === "demo-token") {
      setOrders([]);
      return;
    }
    authApi
      .orders(token)
      .then((list: any) => setOrders(list))
      .catch((e: any) => setError(e.message));
  }, [token]);

  if (!token)
    return (
      <div className="rounded-2xl glass p-6">
        Для перегляду замовлень потрібно <Link className="text-brand-500" to="/login">увійти</Link>.
      </div>
    );

  if (error) return <div className="rounded-2xl glass p-6 text-red-400">{error}</div>;

  return (
    <div className="rounded-2xl glass p-6">
      <h1 className="text-2xl font-bold mb-4">Мої замовлення</h1>
      {orders.length === 0 ? (
        <div className="text-neutral-400">Поки що порожньо.</div>
      ) : (
        <div className="space-y-3">
          {orders.map((o) => (
            <div key={o.id} className="rounded-lg bg-neutral-900 p-4">
              <div className="flex items-center justify-between">
                <div className="font-medium">№ {o.id}</div>
                <div className="text-sm text-neutral-400">{o.status}</div>
              </div>
              <div className="text-sm mt-1">Сума: {o.total.toFixed(2)} $</div>
              <div className="text-xs text-neutral-400 mt-2">
                Товарів: {o.items?.reduce((n: number, it: any) => n + it.quantity, 0)}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}




