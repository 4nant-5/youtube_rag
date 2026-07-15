from langchain_core.documents import Document


class DocumentService:
    """Converts transcript into timestamp-aware LangChain Documents."""

    WINDOW_SIZE = 30  # seconds

    @staticmethod
    def transcript_to_documents(
        transcript: list,
        video_id: str,
    ) -> list[Document]:

        documents = []

        current_text = []

        start_time = None
        end_time = None

        for segment in transcript:

            if start_time is None:
                start_time = segment["start"]

            current_text.append(segment["text"])

            end_time = (
                segment["start"] +
                segment["duration"]
            )

            if end_time - start_time >= DocumentService.WINDOW_SIZE:

                documents.append(
                    Document(
                        page_content=" ".join(current_text),
                        metadata={
                            "video_id": video_id,
                            "start_time": start_time,
                            "end_time": end_time,
                        },
                    )
                )

                current_text = []
                start_time = None

        if current_text:

            documents.append(
                Document(
                    page_content=" ".join(current_text),
                    metadata={
                        "video_id": video_id,
                        "start_time": start_time,
                        "end_time": end_time,
                    },
                )
            )

        return documents