"use client";

import { useState, useEffect } from "react";
import { useSearchParams } from "next/navigation";
import Learn from "../components/dashboard/Learn/Learn";
import Flashcards from "../components/dashboard/Flashcards/Flashcards";
import Quiz from "../components/dashboard/Quiz/Quiz";
import Link from "next/link";
import { PiBookThin } from "react-icons/pi";
import { PiCardsThreeThin } from "react-icons/pi";
import { PiTestTubeThin } from "react-icons/pi";
import logo from "../../public/logo.png";
import Image from "next/image";
import { IoIosLogOut } from "react-icons/io";

export default function Dashboard() {
  const searchParams = useSearchParams();
  const section = searchParams.get("section") || "learn";
  const [activeTab, setActiveTab] = useState(section);

  useEffect(() => {
    setActiveTab(section);
  }, [section]);

  let ContentComponent;
  switch (section) {
    case "flashcards":
      ContentComponent = Flashcards;
      break;
    case "quiz":
      ContentComponent = Quiz;
      break;
    default:
      ContentComponent = Learn;
      break;
  }

  const tabs = [
    {
      id: "learn",
      label: "Learn",
      href: "/dashboard?section=learn",
      icon: <PiBookThin />,
    },
    {
      id: "flashcards",
      label: "Flashcards",
      href: "/dashboard?section=flashcards",
      icon: <PiCardsThreeThin />,
    },
    {
      id: "quiz",
      label: "Quiz",
      href: "/dashboard?section=quiz",
      icon: <PiTestTubeThin />,
    },
  ];

  return (
    <div className="relative overflow-hidden min-h-screen">
      <div className="fixed inset-y-0 left-0 bg-white shadow-md max-h-screen w-60">
        <div className="flex flex-col justify-between h-full">
          <div className="flex-grow">
            <div className="px-4 py-6 border-b">
              <div className="flex items-center justify-center">
                <Image width={50} height={50} src={logo} alt="logo" />
                <Link href="/" className="text-2xl font-normal">
                  smeek
                </Link>
              </div>
            </div>
            <div className="p-4">
              <div className="flex flex-col gap-1">
                {tabs.map((tab) => (
                  <Link
                    key={tab.id}
                    href={tab.href}
                    onClick={() => setActiveTab(tab.id)}
                    className={`flex items-center rounded-xl text-sm font-normal py-3 px-4 gap-4 ${
                      activeTab === tab.id
                        ? "bg-[#333333] text-white"
                        : "text-gray-600"
                    }`}
                  >
                    {tab.icon} {tab.label}
                  </Link>
                ))}
              </div>
            </div>
          </div>
          <div className=" p-4">
            <div className="flex items-center ml-2">
              <IoIosLogOut className="text-black text-xl" />
              <span className="font-medium text-sm ml-2">Logout</span>
            </div>
          </div>
        </div>
      </div>
      <main className="ml-60 pt-16 max-h-screen overflow-auto">
        <ContentComponent />
      </main>
    </div>
  );
}
