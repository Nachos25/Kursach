import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { api, API_BASE } from "../lib/api";

export default function ProductPage() {
  const { slug } = useParams();
  const [p, setP] = useState<any | null>(null);

  useEffect(() => {
    api.get(`/products/${slug}`).then(setP);
  }, [slug]);

  if (!p) return <div className="rounded-xl glass p-6">Завантаження...</div>;

  const finalPrice = Math.round(p.price * (1 - p.discount_percent / 100) * 100) / 100;
  const src = p.image_url
    ? (p.image_url.startsWith("http")
        ? `${API_BASE}/proxy?url=${encodeURIComponent(p.image_url)}`
        : `${API_BASE}/images/${encodeURIComponent(p.image_url)}`)
    : undefined;
  return (
    <div className="rounded-2xl glass p-6 grid grid-cols-1 md:grid-cols-2 gap-6">
      <div className="aspect-square rounded-xl bg-neutral-900 overflow-hidden">
        {/* eslint-disable-next-line jsx-a11y/alt-text */}
        <img src={src} className="object-cover w-full h-full" />
      </div>
      <div>
        <div className="text-neutral-400 text-sm">{p.brand?.name}</div>
        <h1 className="text-3xl font-bold">{p.name}</h1>
        <p className="text-neutral-300 mt-2">{p.short_desc}</p>
        <div className="mt-4 flex items-baseline gap-2">
          <div className="text-3xl font-bold">{finalPrice.toFixed(2)} $</div>
          {p.discount_percent > 0 && (
            <div className="text-neutral-400 line-through">{p.price.toFixed(2)} $</div>
          )}
        </div>
        <button className="mt-6 px-4 py-2 rounded bg-brand-700 hover:bg-brand-600">Додати до кошика</button>

        {p.description && (
          <div className="mt-8">
            <div className="text-sm uppercase tracking-wider text-neutral-400 mb-2">Опис</div>
            <div className="prose prose-invert max-w-none text-neutral-200 whitespace-pre-line">
              {p.description}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}




