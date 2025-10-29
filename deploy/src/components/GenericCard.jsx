import '../css/GenericCard.css'

const banners = import.meta.glob("../assets/*/*/*.webp", { eager: true });

const GenericCard = ({ type, data, onClick}) => {
    let banner = data.banner;
    const bannerUrl = banner && typeof banner === "string" ? banners[`../${banner}`]?.default || banner : banner;
    console.log("BANNER MAPEADO", bannerUrl);

    switch (type) {
        case "projeto":
            return (
                <div className="generic-card">
                    <div className="generic-card-projeto" onClick={() => onClick(data.link)}>
                        <img src={String(bannerUrl)} alt={data.title} loading="lazy" decoding="async"/>
                        <div className="card-content">
                            <h2>{data.title}</h2>
                            <p>{data["subtitle"]}</p>
                        </div>
                    </div>
                </div>
            );

        case "artigo":
            return (
                <div className="generic-card">
                    <div className="generic-card-artigo" onClick={() => onClick(data)}>
                        <img src={String(bannerUrl)} alt={data.title} loading="lazy" decoding="async"/>
                        <div className="card-content">
                            <span>{data.categories}</span>
                            <h3>{data.title}</h3>
                            <p>{data.date}</p>
                        </div>
                    </div>
                </div>
            );

        case "produto":
            return (
                <div className="generic-card">
                    <a href={data.link} target="_blank" rel="noopener noreferrer nofollow external sponsored">
                        <div className="generic-card-produto">
                            <img src={data["link_imagem"]} alt={data["nome"]} loading="lazy" decoding="async"/>
                            <div className="card-content">
                                <h3>{data["nome"]}</h3>
                                <p>{data["descricao"]}</p>
                            </div>
                        </div>
                    </a>
                </div>
            );

        default:
            return null;
    }
};

export default GenericCard;
