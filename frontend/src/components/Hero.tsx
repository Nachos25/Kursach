export default function Hero() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
      <div className="rounded-2xl p-6 glass bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-brand-700/20 to-transparent">
        <div className="text-3xl font-extrabold leading-tight">Щедрі знижки</div>
        <div className="text-neutral-400">до -45% на популярне</div>
        <div className="mt-4 h-28 w-full rounded-xl bg-[url('https://images.unsplash.com/photo-1603903645270-0f0b4ce8b1a7?q=80&w=1200&auto=format&fit=crop')] bg-cover bg-center" />
      </div>
      <div className="rounded-2xl p-6 glass">
        <div className="text-neutral-400 text-sm">Особлива оплата</div>
        <div className="text-2xl font-bold">частинами для iPhone</div>
        <div className="mt-4 h-28 w-full rounded-xl bg-[url('https://images.unsplash.com/photo-1635070041078-e363dbe005cb?q=80&w=1200&auto=format&fit=crop')] bg-cover bg-center" />
      </div>
      <div className="rounded-2xl p-6 glass">
        <div className="text-2xl font-bold">Найкращий під ялинку</div>
        <div className="mt-4 h-28 w-full rounded-xl bg-[url('https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?q=80&w=1200&auto=format&fit=crop')] bg-cover bg-center" />
      </div>
    </div>
  );
}




