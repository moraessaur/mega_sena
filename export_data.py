import tabula
import pandas as pd

pdf_path = 'Todos os resultados da Mega Sena Rede Loteriapesquisar.pdf'
tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
data_frames = [pd.DataFrame(table) for table in tables]

len(data_frames)

combined_df = pd.concat(data_frames, ignore_index=True)

combined_df.to_csv("df.csv")

len(combined_df)

for data_frame in data_frames:
    print(data_frame)
