import { Link } from "react-router-dom";
import { API_BASE } from "../lib/api";

type Product = {
  id: number;
  name: string;
  slug: string;
  price: number;
  discount_percent: number;
  image_url?: string | null;
  short_desc?: string | null;
  in_stock: boolean;
  brand: { name: string };
};

export default function ProductCard({ p }: { p: Product }) {
  const finalPrice = Math.round(p.price * (1 - p.discount_percent / 100) * 100) / 100;
  const src = p.image_url
    ? (p.image_url.startsWith("http")
        ? `${API_BASE}/proxy?url=${encodeURIComponent(p.image_url)}`
        : `${API_BASE}/images/${encodeURIComponent(p.image_url)}`)
    : undefined;
  return (
    <Link to={`/product/${p.slug}`} className="rounded-2xl glass p-4 block hover:bg-white/10">
      <div className="aspect-[4/3] rounded-xl bg-neutral-900 mb-3 overflow-hidden flex items-center justify-center">
        {src ? (
          // eslint-disable-next-line jsx-a11y/alt-text
          <img src={src} className="object-cover w-full h-full" />
        ) : (
          <div className="text-neutral-600">Фото відсутнє</div>
        )}
      </div>
      <div className="text-xs text-neutral-400">{p.brand?.name}</div>
      <div className="font-medium leading-snug line-clamp-2">{p.name}</div>
      <div className="mt-2 flex items-baseline gap-2">
        <div className="text-lg font-bold">{finalPrice.toFixed(2)} $</div>
        {p.discount_percent > 0 && (
          <div className="text-neutral-400 line-through text-sm">{p.price.toFixed(2)} $</div>
        )}
      </div>
    </Link>
  );
}




