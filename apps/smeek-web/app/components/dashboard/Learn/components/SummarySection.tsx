import { useState } from "react";
import axios from "axios";
import Image from "next/image";
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";
import summaryImg from "../../../../../public/summary.png";

interface SummaryProps {
  summary: string;
  loading: boolean;
}

export default function SummarySection({ summary, loading }: SummaryProps) {
  return (
    <>
      <div>
        {/* {loading ? (
          <>
            <div>
              <p className="text-sm font-semibold pt-3">
                Smeek is summarzing... 🧠
              </p>
            </div>
          </>
        ) : ( */}
        <>
          <div className="flex">
            <Image width={700} height={700} src={summaryImg} alt="" />
            <div className="p-3 rounded-lg">
              <Markdown remarkPlugins={[remarkGfm]}>{summary}</Markdown>
            </div>
          </div>
        </>
        {/* )} */}
      </div>
    </>
  );
}
