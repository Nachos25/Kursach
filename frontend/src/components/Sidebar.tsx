import { useEffect, useState } from "react";
import { api } from "../lib/api";
import { Link, useSearchParams } from "react-router-dom";

type Category = { id: number; name: string; slug: string };

export default function Sidebar() {
  const [categories, setCategories] = useState<Category[]>([]);
  const [params] = useSearchParams();
  const active = params.get("category");

  useEffect(() => {
    api.get("/categories").then(setCategories);
  }, []);

  return (
    <div className="rounded-xl p-3 glass sticky top-[68px]">
      <div className="text-sm uppercase tracking-wider text-neutral-400 px-2 pb-2">Категорії</div>
      <nav className="space-y-1">
        {categories.map((c) => (
          <Link
            key={c.id}
            to={`/?category=${c.slug}`}
            className={`block px-3 py-2 rounded hover:bg-white/5 ${active === c.slug ? "bg-white/10" : ""}`}
          >
            {c.name}
          </Link>
        ))}
      </nav>
    </div>
  );
}




