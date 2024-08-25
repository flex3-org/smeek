interface MoreVideosSectionProps {
    links: string[];
}

export default function MoreVideosSection({ links }: MoreVideosSectionProps) {
    return (
        <div className="p-4">
            {links.map((link, index) => (
                <div key={index} className="mb-4">
                    <img
                        className="w-full h-32 object-cover mb-2"
                        src={`https://img.youtube.com/vi/${link.split('v=')[1]}/hqdefault.jpg`}
                        alt={`Video ${index + 2}`}
                    />
                    <a
                        href={link}
                        className="text-blue-300 hover:underline block"
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        Watch Video {index + 2}
                    </a>
                </div>
            ))}
        </div>
    );
}