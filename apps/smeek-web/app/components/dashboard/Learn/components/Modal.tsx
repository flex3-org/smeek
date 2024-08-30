"use client"
import { useState } from "react";
import ChatSection from "./ChatSection";
import TranscribeSection from "./TranscribeSection";
import MoreVideosSection from "./MoreVideosSection";
MoreVideosSection
import { IoClose } from "react-icons/io5";

export default function Modal({ modalContent, closeModal }: any) {
    const [activeSection, setActiveSection] = useState<string>("chat");

    const renderSection = () => {
        switch (activeSection) {
            case "chat":
                return <ChatSection />;
            case "transcribe":
                return <TranscribeSection />;
            case "more-videos":
                return <MoreVideosSection links={modalContent.links.slice(1)} />;
            default:
                return null;
        }
    };

    return (
        <div className="fixed inset-0 flex justify-end items-center bg-black bg-opacity-50 z-50">
            <div className="bg-white w-3/4 h-full p-4 overflow-y-auto" onClick={(e) => e.stopPropagation()}>
                <div className="flex items-center justify-between">
                    <h1 className="text-xl pt-3 font-bold">{modalContent.label} - </h1>
                    <IoClose onClick={closeModal} className="text-xl"/>
                </div>
                <div className="flex items-center justify-center mb-6 pt-8">
                    <iframe
                        className="w-[900px] h-[520px]"
                        src={`https://www.youtube.com/embed/${modalContent.links[0]?.split('v=')[1]}`}
                        title={modalContent.label}
                        allowFullScreen
                    />
                </div>

                {/* Sections Navigation */}
                 <div className="p-4 mb-6">
            <div className="flex gap-5">
                <button 
                    className={`p-2 rounded-none text-center ${activeSection === "chat" ? "border-b-4 border-gray-800" : "text-gray-600"}`}
                    onClick={() => setActiveSection("chat")}
                >
                    Chat
                </button>
                <button 
                    className={`p-2 rounded-none text-center ${activeSection === "transcribe" ? "border-b-4 border-gray-800" : "text-gray-600"}`}
                    onClick={() => setActiveSection("transcribe")}
                >
                    Transcribe
                </button>
                <button 
                    className={`p-2 rounded-none text-center ${activeSection === "more-videos" ? "border-b-4 border-gray-800" : "text-gray-600"}`}
                    onClick={() => setActiveSection("more-videos")}
                >
                    More Videos
                </button>
            </div>
        </div>
                {renderSection()}
            </div>
        </div>
    );
}
