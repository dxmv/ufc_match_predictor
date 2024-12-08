import React from 'react';
import { UFCEvent } from '../types/match_types';
import MatchList from '../components/match_list/MatchList';
import { FaCalendarAlt, FaMapMarkerAlt } from 'react-icons/fa';

const EventPage = ({event}: {event: UFCEvent}) => {

   return (
       <div className="min-h-screen">
           {/* Official background image */}
           <div className="relative h-96 bg-cover bg-center" style={{ backgroundImage: `url(https://dmxg5wxfqgb4u.cloudfront.net/styles/background_image_xl/s3/2024-11/120724-ufc-310-pantoja-vs-asakura-EVENT-ART.jpg?h=d1cb525d&itok=XWZWovZk)` }}>
               {/* Black overlay */}
               <div className="absolute top-0 left-0 w-full h-full bg-black opacity-60 flex flex-col justify-center items-center">
                   <h1 className="text-white text-5xl font-bold mt-10">Name of the event</h1>
                   {/* Date and Location in the same row with icons */}
                   <div className="flex items-center text-white text-lg mt-5">
                       <span className="mr-2">
                           <FaCalendarAlt /> {/* Date icon */}
                       </span>
                       <span className="mr-5">{event.date}</span> {/* Today's date */}
                       <span className="mr-2">
                           <FaMapMarkerAlt /> {/* Location icon */}
                       </span>
                       <span>{event.location}</span> {/* Location */}
                   </div>
               </div>
           </div>
           {/* List of fights */}
           <MatchList matches={event.matches} />
       </div>
   );
};

export default EventPage; 