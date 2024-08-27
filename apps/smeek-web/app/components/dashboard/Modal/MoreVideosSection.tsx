import { useEffect, useState } from 'react';

interface VideoCardProps {
    link: string;
    index: number;
}

function VideoCard({ link, index }: VideoCardProps) {
    const [title, setTitle] = useState<string>("");

    useEffect(() => {
        const fetchVideoTitle = async () => {
            try {
                const videoId = link.split('v=')[1];
                const response = await fetch(`https://noembed.com/embed?url=https://www.youtube.com/watch?v=${videoId}`);
                const data = await response.json();
                setTitle(data.title || `Video ${index + 1}`);
            } catch (error) {
                console.error("Error fetching video title:", error);
                setTitle(`Video ${index + 1}`);
            }
        };

        fetchVideoTitle();
    }, [link, index]);

    return (
        <div className="px-2 border rounded-md shadow-lg">
            <img
                className="w-full h-40 object-cover mb-1"
                src={`https://img.youtube.com/vi/${link.split('v=')[1]}/hqdefault.jpg`}
                alt={`Video ${index + 1}`}
            />
            <a
                href={link}
                className="text-blue-300 hover:underline block mb-1"
                target="_blank"
                rel="noopener noreferrer"
            >
                {title}
            </a>
        </div>
    );
}

export default function VideoGrid({ links }: { links: string[] }) {
    return (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
            {links.map((link, index) => (
                <VideoCard key={index} link={link} index={index} />
            ))}
        </div>
    );
}
