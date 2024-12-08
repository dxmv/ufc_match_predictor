import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Upcoming from './pages/Upcoming';
import Previous from './pages/Previous';
import EventPage from './pages/EventPage';
import { UFCEvent } from './types/match_types';

const App: React.FC = () => {

    const event: UFCEvent = {
        name: "UFC 310",
        date: "2024-12-14",
        location: "Las Vegas, NV",
        matches: [],
    };

    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/upcoming" element={<Upcoming />} />
                <Route path="/previous" element={<Previous />} />
                <Route path="/event/:eventId" element={<EventPage event={event} />} />
            </Routes>
            <Footer />
        </Router>
    );
};

export default App;
