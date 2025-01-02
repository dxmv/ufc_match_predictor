import React from 'react';
import { BrowserRouter as Router, Routes, Route, useParams } from 'react-router-dom';
import Navbar from './components/Navbar';
import Footer from './components/Footer';
import Home from './pages/Home';
import Upcoming from './pages/Upcoming';
import Previous from './pages/Previous';
import EventPage from './pages/EventPage';
import { UFCEvent } from './types/match_types';
import MatchPage from './pages/MatchPage';

const App: React.FC = () => {

    const event: UFCEvent = {
        name: "UFC 310",
        date: "2024-12-14",
        location: "Las Vegas, NV",
        matches: [],
    };

    const MatchPageWrapper = ({ upcoming }: { upcoming: boolean }) => {
        const { matchId } = useParams<{ matchId: string }>();
        return <MatchPage matchId={matchId || '0'} upcoming={upcoming} />;
    };

    return (
        <Router>
            <Navbar />
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/upcoming" element={<Upcoming />} />
                <Route path="/previous" element={<Previous />} />
                <Route path="/event/:eventId" element={<EventPage event={event} />} />
                <Route path="/match/upcoming/:matchId" element={<MatchPageWrapper upcoming={true} />} />
                <Route path="/match/:matchId" element={<MatchPageWrapper upcoming={false} />} />
            </Routes>
            <Footer />
        </Router>
    );
};

export default App;
