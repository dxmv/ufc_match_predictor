const WinnerSquare = ({ blue }: { blue?: boolean }) => {
    return (
        <div className={`absolute top-0 ${blue ? 'right-0' : 'left-0'} w-10 h-10 bg-yellow-500 rounded-md flex items-center justify-center text-white font-bold`}>
            W
        </div>
    );
};

export default WinnerSquare;