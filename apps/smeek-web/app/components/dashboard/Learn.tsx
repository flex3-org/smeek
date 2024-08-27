"use client";
import axios from "axios";
import { useState } from "react";
import { FaSearch } from "react-icons/fa";
import Skeleton from 'react-loading-skeleton';
import 'react-loading-skeleton/dist/skeleton.css';
import ReactFlow, { MiniMap, Controls, Background } from 'reactflow';
import 'reactflow/dist/style.css';
import Modal from "./Modal/Modal";
import { data } from "@/utils/data";

interface CourseContent {
    index: number;
    topic: string;
    link: string[];  // Updated to handle multiple links
}

export default function Quiz() {
    const [topic, setTopic] = useState<string>("");
    // const [data, setData] = useState<CourseContent[]>([]);
    const [loading, setLoading] = useState<boolean>(false);
    const [nodes, setNodes] = useState<any[]>([]);
    const [edges, setEdges] = useState<any[]>([]);
    const [modalContent, setModalContent] = useState<{ label: string; links: string[] } | null>(null);

    const getCourseContent = async (e: React.FormEvent<HTMLButtonElement>) => {
        e.preventDefault();
        setLoading(true);

        try {
            // const res = await axios.get<CourseContent[]>("http://127.0.0.1:8000/coursecontents", {
            //     params: { topic: topic }
            // });
            const fetchedData = data;  // Fetch data correctly

            // Create nodes with increased spacing between rows
            const newNodes = fetchedData.map((item, index) => ({
                id: `${index + 1}`,
                data: {
                    label: item.topic,
                    links: item.link
                },
                position: { x: (index % 4) * 200, y: Math.floor(index / 4) * 120 },  // Increase y-value for more spacing
            }));

            // Create edges (update logic as needed)
            const newEdges = fetchedData.slice(1).map((_, index) => ({
                id: `e${index}-${index + 1}`,
                source: `${index + 1}`,
                target: `${index + 2}`,
                animated: true,
            }));

            setNodes(newNodes);
            setEdges(newEdges);
            setData(fetchedData);
        } catch (err) {
            console.error(err);
        } finally {
            setLoading(false);
        }
    }

    const onNodeClick = (event: any, node: any) => {
        setModalContent({
            label: node.data.label,
            links: node.data.links
        });
    };

    const closeModal = () => {
        setModalContent(null);
    };

    return (
        <>
            <div className="px-12">
                <div className="flex justify-center items-center gap-2">
                    <input
                        className="border border-gray-200 w-[500px] px-2 py-2 rounded-full focus:outline-none"
                        type="text"
                        placeholder="What do you want to learn today?"
                        onChange={(e) => setTopic(e.target.value)}
                    />
                    <button
                        className="bg-[#333333] px-6 py-1 text-white rounded-md flex items-center gap-1"
                        onClick={getCourseContent}
                    >
                        Learn <FaSearch size={16} />
                    </button>
                </div>

                {loading ? (
                    <div className="mt-24">
                        <Skeleton count={10} height={50} />
                    </div>
                ) : (
                    <div className="relative h-[900px] mt-24">
                        <ReactFlow
                            nodes={nodes}
                            edges={edges}
                            onNodeClick={onNodeClick}
                        >
                            <MiniMap />
                            <Controls />
                        </ReactFlow>
                    </div>
                )}

                {modalContent && (
                    <div className="fixed inset-0 flex justify-end items-center bg-black bg-opacity-50 cursor-pointer z-50" onClick={closeModal}>
                        <div className="bg-black w-3/4 h-full p-4 overflow-y-auto" onClick={(e) => e.stopPropagation()}>
                            <h2 className="text-white text-lg font-semibold mb-4">{modalContent.label}</h2>
                            {modalContent && (
                                <Modal modalContent={modalContent} closeModal={closeModal} />
                            )}

                        </div>
                    </div>
                )}
            </div>
        </>
    );
}

