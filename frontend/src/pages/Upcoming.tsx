import React, { useEffect, useState } from 'react';
import EventPage from './EventPage';
import { UFCEvent } from '../types/match_types';
import { fetchUpcomingMatches } from '../services/api/matchesApi';
import Loading from '../components/Loading';

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
        <>
            {event ? <EventPage event={event} upcoming={true} /> : <Loading />}
        </>
    );
};

export default Upcoming;