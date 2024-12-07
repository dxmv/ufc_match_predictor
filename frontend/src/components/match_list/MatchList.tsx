import { Match } from '../../types/match_types';

import MatchCard from './MatchCard';

const MatchList = ({ matches }: { matches: Match[] }) => {
    return <div className='flex flex-col items-center justify-center pb-10 px-12 w-100'>{matches.map((match) => <MatchCard match={match} />)}</div>;
};

export default MatchList;