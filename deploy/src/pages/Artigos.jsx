import React, {useCallback, useEffect, useRef, useState} from "react";
import GenericCard from "../components/GenericCard";
import ArtigoMarkdown from "../components/ArtigoMarkdown.jsx";
import Buscador from "../components/Buscador.jsx";
import artigosData from "../assets/artigos.json";

// eslint-disable-next-line
import { motion, AnimatePresence } from "framer-motion";

const markdownFiles = import.meta.glob("../assets/artigos/*/*.md", { import: "default", query: "?raw" });
let artigosCache = artigosData || [];

const Artigos = () => {
    const [artigos] = useState(artigosCache);
    const [filteredArtigos, setFilteredArtigos] = useState([]);
    const [selectedArticle, setSelectedArticle] = useState(null);
    const [articleContent, setArticleContent] = useState("");
    const firstRenderRef = useRef(true);

    const openArticle = useCallback(async (artigo) => {
        firstRenderRef.current = false;
        setSelectedArticle(artigo);
        setArticleContent("");

        const path = `../${artigo.link}`;
        const loader = markdownFiles[path];

        if (loader) {
            try {
                const md = await loader();
                setArticleContent(md);
            } catch (err) {
                console.error("Erro ao carregar markdown:", err);
            }
        } else {
            console.error("Markdown não encontrado:", path);
        }

        const url = new URL(window.location);
        url.searchParams.set("artigo", encodeURIComponent(artigo.title));
        window.history.replaceState({}, "", url);
    }, []);

    useEffect(() => {
        if (artigos.length === 0) return;
        const params = new URLSearchParams(window.location.search);
        const artigoId = params.get("artigo");
        if (!artigoId) return;

        const artigo = artigos.find((a) => encodeURIComponent(a.title) === artigoId);
        if (artigo) {
            openArticle(artigo).then();
        }
    }, [artigos, openArticle]);

    const backToList = () => {
        setSelectedArticle(null);
        setArticleContent("");

        const url = new URL(window.location);
        url.searchParams.delete("artigo");
        window.history.replaceState({}, "", url);
    };

    if (new URLSearchParams(window.location.search).get("artigo") && !selectedArticle) {
        return <></>;
    }

    return (
        <div className="page">
            <div className="content-open">
                <AnimatePresence mode="wait">
                    {selectedArticle ? (
                        <motion.div
                            key="detalhe"
                            initial={firstRenderRef.current ? false : { opacity: 0, x: 40 }}
                            animate={{ opacity: 1, x: 0 }}
                            exit={{ opacity: 0, x: 40 }}
                            transition={{ duration: 0.4 }}
                        >
                            <ArtigoMarkdown
                                artigo={selectedArticle}
                                conteudo={articleContent}
                                onBack={backToList}
                                banner={selectedArticle.banner}
                            />
                        </motion.div>
                    ) : (
                        <div>
                            <motion.div
                                key="lista"
                                initial={firstRenderRef.current ? false : { opacity: 0, x: -40 }}
                                animate={{ opacity: 1, x: 0 }}
                                exit={{ opacity: 0, x: -40 }}
                                transition={{ duration: 0.4 }}
                            >
                                <Buscador data={artigos} onFilter={setFilteredArtigos} />
                                <div className="top-section">
                                    {filteredArtigos.map((artigo) => (
                                        <GenericCard
                                            key={artigo.title}
                                            type="artigo"
                                            data={artigo}
                                            onClick={openArticle}
                                        />
                                    ))}
                                </div>
                            </motion.div>
                        </div>
                    )}
                </AnimatePresence>
            </div>
        </div>
    );
}

export default Artigos;
