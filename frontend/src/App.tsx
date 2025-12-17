import { Outlet, Link, useNavigate, useLocation } from "react-router-dom";
import Sidebar from "./components/Sidebar";
import BrandRow from "./components/BrandRow";
import Hero from "./components/Hero";
import { getToken, logout } from "./lib/auth";

function NavItem({ to, children }: { to: string; children: React.ReactNode }) {
  const location = useLocation();
  const active = location.pathname === to || (to === "/" && location.pathname === "/");
  return (
    <Link to={to} className="nav-link" data-active={active}>
      {children}
    </Link>
  );
}

export default function App() {
  const navigate = useNavigate();
  const location = useLocation();
  const authed = Boolean(getToken());

  const onLogout = () => {
    logout();
    navigate("/");
  };

  return (
    <div className="min-h-screen">
      <header className="sticky top-0 z-40 bg-neutral-950/90 border-b border-white/10 backdrop-blur">
        <div className="max-w-7xl mx-auto px-4 py-3 flex items-center gap-4">
          <Link to="/" className="font-bold text-xl tracking-wide">
            Perforator
          </Link>

          <NavItem to="/">Каталог</NavItem>

          <div className="ml-auto flex items-center gap-2">
            {authed ? (
              <>
                <NavItem to="/profile">Профіль</NavItem>
                <button onClick={onLogout} className="px-3 py-1 rounded bg-brand-700 hover:bg-brand-600">
                  Вийти
                </button>
              </>
            ) : (
              <>
                <NavItem to="/login">Увійти</NavItem>
                <Link to="/register" className="px-3 py-1 rounded bg-brand-700 hover:bg-brand-600">Реєстрація</Link>
              </>
            )}
          </div>
        </div>
      </header>

      <main className="max-w-7xl mx-auto px-4 py-6 grid grid-cols-12 gap-6">
        <aside className="col-span-12 lg:col-span-3">
          <Sidebar />
        </aside>
        <section className="col-span-12 lg:col-span-9 space-y-6">
          <Hero />
          <BrandRow />
          <Outlet />
        </section>
      </main>

      <footer className="border-t border-white/10 py-8 text-center text-sm text-neutral-400">
        © {new Date().getFullYear()} Perforator. Всі права захищені.
      </footer>
    </div>
  );
}




