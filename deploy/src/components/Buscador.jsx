import React, { useEffect, useState } from "react";
import '../css/Buscador.css'

const Buscador = ({ data = [], onFilter }) => {
    const [search, setSearch] = useState("");
    const [category, setCategory] = useState("todas");
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        const params = new URLSearchParams(window.location.search);
        const s = params.get("busca") || "";
        const c = params.get("categoria") || "todas";
        setSearch(s);
        setCategory(c);
    }, []);

    useEffect(() => {
        const uniqueCategories = Array.from(
            new Set(
                data.flatMap((item) =>
                    (item.categories || "")
                        .split(",")
                        .map((c) => c.trim())
                        .filter((c) => c.length > 0)
                )
            )
        );
        setCategories(uniqueCategories);
    }, [data]);

    useEffect(() => {
        const term = search.toLowerCase();
        const filtered = data.filter((item) => {
            const titleMatch = item.title.toLowerCase().includes(term);
            const categoryMatch =
                category === "todas" ||
                (item.categories &&
                    item.categories.toLowerCase().includes(category.toLowerCase()));
            return titleMatch && categoryMatch;
        });

        onFilter(filtered);

        const params = new URLSearchParams(window.location.search);
        if (search) params.set("busca", search);
        else params.delete("busca");

        if (category && category !== "todas") params.set("categoria", category);
        else params.delete("categoria");

        const url = `${window.location.pathname}?${params.toString()}`;
        window.history.replaceState({}, "", url);
    }, [search, category, data, onFilter]);

    return (
        <div className="buscador">
            <input
                type="text"
                placeholder="Buscar artigo..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                className="buscador-input"
            />
            <div className="buscador-select-wrapper">
                <select
                    value={category}
                    onChange={(e) => setCategory(e.target.value)}
                    className="buscador-select"
                >
                    <option value="todas">Todos</option>
                    {categories.map((cat) => (
                        <option key={cat} value={cat}>
                            {cat}
                        </option>
                    ))}
                </select>
            </div>
        </div>
    );
};

export default Buscador;
