import Tabs from './components/Tabs';
import Tab from './components/Tab';
import TabPanel from './components/TabPanel';

import {lazy} from "react";
const Inicio = lazy(() => import('./pages/Inicio'));
const Produtos = lazy(() => import('./pages/Produtos'));
const Projetos = lazy(() => import('./pages/Projetos'));
const Artigos = lazy(() => import('./pages/Artigos'));

import homeIcon from './assets/home.svg';
import produtosIcon from './assets/products.svg';
import projetosIcon from './assets/projects.svg';
import artigosIcon from './assets/articles.svg';

import './css/App.css'

function App() {
    return (
        <div className="app-container">
            <Tabs defaultIndex={0}>
                <Tab label="Home" icon={homeIcon} />
                <Tab label="Produtos" icon={produtosIcon} />
                <Tab label="Projetos" icon={projetosIcon} />
                <Tab label="Artigos" icon={artigosIcon} />
                <TabPanel><Inicio /></TabPanel>
                <TabPanel><Produtos /></TabPanel>
                <TabPanel><Projetos /></TabPanel>
                <TabPanel><Artigos /></TabPanel>
            </Tabs>
        </div>
    );
}

export default App;
