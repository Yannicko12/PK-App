'use client'

import { useEffect, useState } from "react";

type Post = {
    id: number,
    title: { rendered: string }
    content: { rendered: string }
}

export default function HomePage() {
    const [posts, setPosts] = useState<Post[]>([]);
    const [error, setError] = useState<string | null>(null)
    useEffect(() => {
        fetch("http://mediplus-cvo.de/wp-json/wp/v2/posts")
            .then((res) => {
                if (!res.ok) {
                    throw new Error("HTTP error! status: ${res.status}");
                }
                return res.json();
            })
            .then((data: Post[]) => setPosts(data))
            .catch((err) => {
                console.error(err);
                setError("Fehler beim Laden.");
            })
    }, [])

    return (
        <div style={{ padding: "2rem" }}>
            <h1>WordPress Beiträge</h1>
            {error && <p style={{ color: "red" }}></p>}
            {posts.map((post) => (
                <div key={post.id} style={{ marginBottom: "2rem" }}>
                    <h2 dangerouslySetInnerHTML={{ __html: post.title.rendered }} />
                    <div dangerouslySetInnerHTML={{ __html: post.content.rendered }}/>  
                </div>
            ))}
        </div>
    )
} 
