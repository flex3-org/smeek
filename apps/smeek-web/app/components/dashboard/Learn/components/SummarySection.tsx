import { useState } from "react";
import axios from "axios";
import Markdown from "react-markdown";
import remarkGfm from "remark-gfm";

interface VideoLinkProps {
  link: string;
}

export default function SummarySection({ link }: VideoLinkProps) {
  const [loading, setLoading] = useState<boolean>(false);
  const [summary, setSummary] = useState<string>("");

  const getSummary = async () => {
    try {
      setLoading(true); // Set loading to true when starting request
      const res = await axios.get("http://127.0.0.1:8000/summary", {
        params: {
          url: link,
        },
      });
      console.log(res.data);
      setSummary(res.data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false); // Set loading to false when request is complete
    }
  };
  return (
    <>
      <div>
        <button
          className="bg-[#333333] px-6 py-1 text-white rounded-md flex items-center gap-1"
          onClick={getSummary}
        >
          Learn
        </button>
        <div className="flex">
          <div className="p-3 rounded-lg">
            <Markdown remarkPlugins={[remarkGfm]}>{summary}</Markdown>
          </div>
        </div>
      </div>
    </>
  );
}
