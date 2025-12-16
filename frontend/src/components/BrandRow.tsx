import { useEffect, useState } from "react";
import { api } from "../lib/api";

type Brand = { id: number; name: string; slug: string; logo_url?: string | null };

export default function BrandRow() {
  const [brands, setBrands] = useState<Brand[]>([]);

  useEffect(() => {
    api.get("/brands").then(setBrands);
  }, []);

  return (
    <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-3">
      {brands.map((b) => (
        <div key={b.id} className="rounded-xl glass px-4 py-5 text-center hover:bg-white/10 transition">
          <div className="h-10 flex items-center justify-center">
            {b.logo_url ? (
              // eslint-disable-next-line @next/next/no-img-element
              <img src={b.logo_url} className="max-h-8 opacity-80" alt={b.name} />
            ) : (
              <div className="text-neutral-300 font-semibold">{b.name}</div>
            )}
          </div>
        </div>
      ))}
    </div>
  );
}




