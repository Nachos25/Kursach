import { useEffect, useState } from "react";
import { api } from "../lib/api";
import ProductCard from "../components/ProductCard";
import { useSearchParams } from "react-router-dom";

type Product = any;

export default function CatalogPage() {
  const [products, setProducts] = useState<Product[]>([]);
  const [params] = useSearchParams();

  useEffect(() => {
    const q = params.get("q") || "";
    const category = params.get("category") || "";
    const brand = params.get("brand") || "";
    const s = new URLSearchParams();
    if (q) s.set("q", q);
    if (category) s.set("category", category);
    if (brand) s.set("brand", brand);

    api.get(`/products?${s.toString()}`).then(setProducts).catch(console.error);
  }, [params]);

  return (
    <div className="space-y-3">
      <div className="flex items-center gap-2">
        <input
          className="w-full rounded-lg bg-neutral-900 border border-white/10 px-3 py-2 outline-none"
          placeholder="Пошук товарів..."
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              const v = (e.target as HTMLInputElement).value;
              const s = new URLSearchParams(params);
              if (v) s.set("q", v);
              else s.delete("q");
              window.location.search = s.toString();
            }
          }}
        />
      </div>

      <div className="grid grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-4">
        {products.map((p) => (
          <ProductCard key={p.id} p={p} />
        ))}
      </div>
    </div>
  );
}




