import {memo} from 'react';
import GenericCard from "./GenericCard";

const ItemList = ({ title, type, items}) => {
    return (
        <div>
            {title && <h2>{title}</h2>}
            <div className="item-list">
                {items.map((item, index) => (
                    <GenericCard key={index} type={type} data={item} />
                ))}
            </div>
        </div>
    );
};

export default memo(ItemList);