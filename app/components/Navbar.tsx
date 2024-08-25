import Link from "next/link"

export default function Navbar() {
    return (
        <>
            <div className="flex items-center justify-between p-6">
                <div><p className="text-xl font-bold">education.ai</p></div>
                <div className="flex items-center gap-8 0">
                    <p className="hidden md:block">Features</p>
                    <Link href="/dashboard" className="py-2 px-4 bg-[#FB411F] text-white rounded-full">Try for free</Link>
                </div>
            </div>
        </>
    )
}
