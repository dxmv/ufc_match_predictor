import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Upcoming from './pages/Upcoming';
import Previous from './pages/Previous';

const App: React.FC = () => {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/upcoming" element={<Upcoming />} />
                <Route path="/previous" element={<Previous />} />
            </Routes>
            <Footer />
        </Router>
    );
};

export default App;
