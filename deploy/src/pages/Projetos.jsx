import React, {useCallback, useRef, useState} from "react";
import GenericCard from "../components/GenericCard";
import ArtigoMarkdown from "../components/ArtigoMarkdown.jsx";
import projetosData from "../assets/projetos.json";

// eslint-disable-next-line
import { motion, AnimatePresence } from "framer-motion";

const markdownFiles = import.meta.glob("../assets/projetos/*/*.md", { import: "default", query: "?raw" });
let projetosCache = projetosData || [];

const Projetos = () => {
    const [projetos] = useState(projetosCache);
    const [selectedProjeto, setSelectedProjeto] = useState(null);
    const [conteudoContent, setConteudoContent] = useState("");
    const firstRenderRef = useRef(true);

    const handleOpenProjeto = useCallback(async (projeto) => {
        firstRenderRef.current = false;
        setSelectedProjeto(projeto);
        setConteudoContent("");

        const path = `../${projeto.link}`;
        const loader = markdownFiles[path];

        if (loader) {
            try {
                const md = await loader();
                setConteudoContent(md);
            } catch (err) {
                console.error("Erro ao carregar markdown:", err);
            }
        } else {
            console.error("Markdown não encontrado:", path);
        }
    }, []);

    const backToList = () => {
        setSelectedProjeto(null);
        setConteudoContent("");
    };

    return (
        <div className="page">
            <div className="content-open">
                <AnimatePresence mode="wait">
                    {selectedProjeto ? (
                        <motion.div
                            key="detalhe"
                            initial={firstRenderRef.current ? false : { opacity: 0, x: 40 }}
                            animate={{ opacity: 1, x: 0 }}
                            exit={{ opacity: 0, x: 40 }}
                            transition={{ duration: 0.4 }}
                        >
                            <ArtigoMarkdown
                                artigo={{
                                    title: selectedProjeto.title,
                                    categories: "",
                                    date: "",
                                }}
                                conteudo={conteudoContent}
                                onBack={backToList}
                                banner={selectedProjeto.banner}
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
                                <div className="top-section top-column">
                                    {projetos.map((p) => (
                                        <GenericCard key={p.title} type="projeto" data={p} onClick={() => handleOpenProjeto(p)}/>
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

export default Projetos;
