import ReactMarkdown from 'react-markdown';
import remarkGfm from "remark-gfm";

import icon from "../assets/back.svg";
import '../css/ArtigoMarkdown.css';
import '../css/ArtigoMD.css';

// 1. O glob deve ser o mais específico possível, mas abrangente para todos os seus assets.
// O caminho deve ser relativo ao arquivo atual.
// Exemplo: Se suas imagens de artigo estão em 'assets/artigos/nome-do-artigo/image.png'
const images = import.meta.glob("../assets/**/*.{png,gif,webp,jpg,jpeg}", { eager: true });

// 2. Componente Customizado para a Imagem
// Ele recebe as props do nó de imagem do Markdown.
const ImageRenderer = ({ src, alt }) => {
    // 2.1. Lógica para encontrar o URL real da imagem no mapa 'images'.
    // O 'src' do Markdown pode ser 'image.gif', 'pasta/image.png', etc.
    // É necessário encontrar a chave (caminho completo) que termina com este 'src'.

    // Remove `./` ou outros prefixos comuns para facilitar a correspondência.
    const normalizedSrc = src.startsWith('./') ? src.substring(2) : src;

    // Procura a chave no objeto 'images' que termina com o 'normalizedSrc'.
    const imageKey = Object.keys(images).find(key => key.endsWith(normalizedSrc));

    // Se a chave for encontrada, usa o 'default' (que é a URL tratada pelo bundler).
    // Caso contrário, usa o 'src' original (útil para URLs externas).
    const finalSrc = imageKey ? images[imageKey].default : src;

    return (
        <img
            src={finalSrc}
            alt={alt || ''}
            className="artigo-markdown-image" // Adicione estilos CSS se necessário
            loading="lazy"
            style={{ maxWidth: '100%', height: 'auto' }} // Garante que a imagem é responsiva
        />
    );
};


const ArtigoMarkdown = ({ artigo, conteudo, onBack, banner }) => {
    // A lógica do banner usa o mesmo mapa de imagens, o que é consistente.
    const bannerUrl = banner && typeof banner === 'string' ? images[`../${banner}`]?.default || banner : banner;
    console.log("BANNER MAPEADO", bannerUrl);

    // 3. Define os custom components, usando o nosso ImageRenderer para a tag 'img'.
    const customComponents = {
        img: ImageRenderer,
        // Você pode adicionar outros elementos se precisar (ex: a: LinkRenderer)
    };

    return (
        <div className="artigo-markdown-scroll">
            <div className="artigo-markdown">
                <div className="artigo-markdown-border">
                    <div className="artigo-markdown-voltar-wrapper">
                        <button className="artigo-markdown-voltar" onClick={onBack}>
                            <img src={String(icon)} alt="Voltar" className="icone-voltar" />
                        </button>
                    </div>

                    {bannerUrl && (
                        <img className="artigo-markdown-banner" src={bannerUrl} alt={artigo.title} />
                    )}

                    <div className="generic-card-artigo artigo-markdown-content">
                        {artigo.categories && (<span>{artigo.categories}</span>)}
                        <h1>{artigo.title}</h1>
                        {artigo.date && (<p>{artigo.date}</p>)}
                    </div>

                    <div className="artigo-md">
                        <ReactMarkdown
                            remarkPlugins={[remarkGfm]}
                            components={customComponents}
                        >
                            {conteudo}
                        </ReactMarkdown>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ArtigoMarkdown;