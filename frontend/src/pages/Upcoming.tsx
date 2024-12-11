import React, { useEffect, useState } from 'react';
import EventPage from './EventPage';
import { UFCEvent } from '../types/match_types';
import { fetchUpcomingMatches } from '../services/api/matchesApi';

const Upcoming: React.FC = () => {
    const [event, setEvent] = useState<UFCEvent | null>(null);

    useEffect(() => {
        const fetchEvent = async () => {
            const matches = await fetchUpcomingMatches();
            setEvent({
                name: "UFC 310",
                date: "2024-12-14",
                location: "Las Vegas, NV",
                matches: matches,
            });
        };
        fetchEvent();
    },[]);

    return (
        <div>
            {event ? <EventPage event={event} /> : <div>Loading...</div>}
        </div>
    );
};

export default Upcoming;