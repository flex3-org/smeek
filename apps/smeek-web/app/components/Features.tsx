import React from "react";
import { FaBookReader } from "react-icons/fa";
import { PiCardsFill } from "react-icons/pi";
import { MdQuiz } from "react-icons/md";

const featuresData = [
  {
    icon: FaBookReader,
    title: "Learn",
    description:
      "Meticulously plan and execute a diverse range of events, from workshops to hosting challenges, fostering hands-on learning experiences.",
  },
  {
    icon: PiCardsFill,
    title: "Flashcards",
    description:
      "Create a platform for educators to share their knowledge and engage with learners, providing valuable insights and guidance.",
  },
  {
    icon: MdQuiz,
    title: "Quiz",
    description:
      "Encourage coding practices and projects by organizing coding sessions, hackathons, and collaborative development opportunities.",
  },
];

export default function Features() {
  return (
    <>
      <div className="h-screen">
        <h1 className="text-center text-4xl font-bold md:pt-32 pt-8">
          Features
        </h1>
        <div className="flex justify-center items-center lg:px-24 px-5 pt-8">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
            {featuresData.map((feature, index) => (
              <div
                key={index}
                className="bg-[#F6F6F7] p-2 rounded-lg hover:bg-gray-200"
              >
                <div className="mt-4">
                  <div className="p-3">
                    <div className="flex items-center gap-3">
                      <feature.icon className="text-xl" />
                      <h1 className="font-semibold text-xl">{feature.title}</h1>
                    </div>
                    <p className="text-sm mt-2">{feature.description}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </>
  );
}
