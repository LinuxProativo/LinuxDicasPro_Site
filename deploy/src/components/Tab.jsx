import React from "react";

const Tab = ({ label, icon, isActive, onClick }) => {
    const className = `tab-item ${isActive ? "active" : ""}`;

    return (
        <li className={className} onClick={onClick}>
            {icon && <img src={icon} alt={label} className="tab-icon" />}
            <span className="tab-label">{label}</span>
        </li>
    );
};

Tab.displayName = "Tab";

export default Tab;
