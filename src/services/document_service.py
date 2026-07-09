from langchain_core.documents import Document


class DocumentService:

    @staticmethod
    def transcript_to_document(
        transcript: list,
        video_id: str,
    ) -> Document:

        full_text = " ".join(
            segment["text"]
            for segment in transcript
        )

        return Document(
            page_content=full_text,
            metadata={
                "video_id": video_id
            }
        )