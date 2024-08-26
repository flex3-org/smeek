"use client"

import { useSearchParams } from 'next/navigation';
import Learn from '../components/dashboard/Learn';
import Flashcards from '../components/dashboard/Flashcards';
import Quiz from '../components/dashboard/Quiz';
import Link from 'next/link';
import { PiBookThin } from "react-icons/pi";
import { PiCardsThreeThin } from "react-icons/pi";
import { PiTestTubeThin } from "react-icons/pi";


export default function Dashboard() {
    const searchParams = useSearchParams();
    const section = searchParams.get('section');

    let ContentComponent;
    switch (section) {
        case 'flashcards':
            ContentComponent = Flashcards;
            break;
        case 'quiz':
            ContentComponent = Quiz;
            break;
        default:
            ContentComponent = Learn;
            break;
    }

    return (
        <div className="relative overflow-hidden min-h-screen">
            <div className="fixed inset-y-0 left-0 bg-white shadow-md max-h-screen w-60">
                <div className="flex flex-col justify-between h-full">
                    <div className="flex-grow">
                        <div className="px-4 py-6 text-center border-b">
                            <h1 className="text-xl font-normal">📚 education.ai</h1>
                        </div>
                        <div className="p-4">
                            <div className="flex flex-col gap-1">
                                <Link href="/dashboard?section=learn" className="flex items-center rounded-xl text-sm font-normal py-3 px-4 gap-4">
                                <PiBookThin/> Learn
                                </Link>
                                <Link href="/dashboard?section=flashcards" className="flex items-center rounded-xl text-sm font-normal py-3 px-4 gap-4">
                                    <PiCardsThreeThin/> Flashcards
                                </Link>
                                <Link href="/dashboard?section=quiz" className="flex items-center rounded-xl text-sm font-normal py-3 px-4 gap-4">
                                    <PiTestTubeThin/> Quiz
                                </Link>
                            </div>
                        </div>
                    </div>
                    <div className="p-4">
                        <button type="button" className="inline-flex items-center justify-center h-9 px-4 rounded-xl bg-gray-900 text-gray-300 hover:text-white text-sm font-semibold transition">
                            <svg xmlns="http://www.w3.org/2000/svg" width="1em" height="1em" fill="currentColor" className="" viewBox="0 0 16 16">
                                <path d="M12 1a1 1 0 0 1 1 1v13h1.5a.5.5 0 0 1 0 1h-13a.5.5 0 0 1 0-1H3V2a1 1 0 0 1 1-1h8zm-2 9a1 1 0 1 0 0-2 1 1 0 0 0 0 2z" />
                            </svg>
                        </button> <span className="font-bold text-sm ml-2">Logout</span>
                    </div>
                </div>
            </div>
            <main className="ml-60 pt-16 max-h-screen overflow-auto">
                <ContentComponent />
            </main>
        </div>
    );
}