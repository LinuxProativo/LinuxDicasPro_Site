import React, { useState, useEffect } from 'react';
import '../css/SideMenu.css'
import icon from "../assets/menu.svg";

const Tabs = ({ children, defaultIndex = 0 }) => {
    const [activeIndex, setActiveIndex] = useState(defaultIndex);
    const [isMobile, setIsMobile] = useState(window.innerWidth < 600);
    const [menuOpen, setMenuOpen] = useState(false);

    const tabs = React.Children.toArray(children).filter(
        (child) => React.isValidElement(child) && child["type"]["displayName"] === 'Tab'
    );

    const panels = React.Children.toArray(children).filter(
        (child) => React.isValidElement(child) && child["type"]["displayName"] === 'TabPanel'
    );

    useEffect(() => {
        const handleResize = () => setIsMobile(window.innerWidth < 600);
        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, []);

    useEffect(() => {
        const params = new URLSearchParams(window.location.search);
        const tab = params.get("tab");

        if (tab) {
            const index = tabs.findIndex(
                (t) => t["props"].label.toLowerCase().includes(tab.toLowerCase())
            );
            if (index >= 0) setActiveIndex(index);
        }
    }, [tabs]);

    const handleTabClick = (index, label) => {
        setActiveIndex(index);
        setMenuOpen(false);

        const url = new URL(window.location);
        url.searchParams.set("tab", label.toLowerCase().replace(/\s+/g, ""));
        window.history.replaceState({}, "", url);
    };

    return (
        <div className="tabs-container">
            {isMobile ? (
                <div>
                    <div className="menu-toggle-wrapper">
                        <button className="menu-toggle"
                            onClick={() => setMenuOpen((prev) => !prev)}
                            aria-expanded={menuOpen} aria-label="Alternar Abas">
                            <img src={String(icon)} alt="Menu" className="icone-voltar" />
                        </button>
                    </div>
                    <nav className={`side-menu ${menuOpen ? "open" : ""}`}>
                        <ul>
                            {tabs.map((tab, index) => (
                                <li
                                    key={index}
                                    className={index === activeIndex ? "active" : ""}
                                    onClick={() => handleTabClick(index, tab["props"].label)}
                                >
                                    {icon && <img src={tab["props"].icon} alt={tab["props"].label} className="tab-icon" />}
                                    {tab["props"].label}
                                </li>
                            ))}
                        </ul>
                    </nav>
                </div>
            ) : (
                <ul className="tabs-list">
                    {tabs.map((tab, index) =>
                        React.cloneElement(tab, {
                            key: index,
                            isActive: index === activeIndex,
                            onClick: () => handleTabClick(index, tab["props"].label),
                        })
                    )}
                </ul>
            )}

            <div className="tabs-content">
                {panels[activeIndex] || null}
            </div>
        </div>
    );
};

export default Tabs;
