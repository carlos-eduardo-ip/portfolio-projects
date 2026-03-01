import pandas as pd
from pathlib import Path
from ..common.logger import Logger

class DataAnalysisService:
    def __init__(self):
        self.logger = Logger.get_logger("DataAnalysis")

    def analyze_uber_data(self, file_path: Path):
        self.logger.info(f"Iniciando análise do arquivo: {file_path.name}")
        
        try:
            df = pd.read_csv(file_path)
            
            total_bookings = len(df)
            
            status_col = None
            for col in df.columns:
                if 'status' in col.lower():
                    status_col = col
                    break
            
            if not status_col:
                self.logger.warning("Coluna de status não encontrada. Usando dados fictícios baseados no exemplo.")
                self.logger.info("\nEstatísticas Principais (Formatado):\n"
                                f"Total de Viagens: {total_bookings}\n"
                                "Nota: Coluna de status não identificada automaticamente.")
                return

            completed = df[df[status_col].str.contains('Completed', case=False, na=False)]
            cancelled = df[df[status_col].str.contains('Cancelled', case=False, na=False)]
            
            customer_cancelled = df[df[status_col].str.contains('Customer', case=False, na=False)]
            driver_cancelled = df[df[status_col].str.contains('Driver', case=False, na=False)]

            success_rate = (len(completed) / total_bookings) * 100
            cancellation_rate = (len(cancelled) / total_bookings) * 100
            customer_cancel_rate = (len(customer_cancelled) / total_bookings) * 100
            driver_cancel_rate = (len(driver_cancelled) / total_bookings) * 100

            stats = (
                f"\n{'='*30}\n"
                f"Estatísticas Principais:\n"
                f"Total de Viagens: {total_bookings}\n"
                f"Taxa de Sucesso: {success_rate:.2f}% ({len(completed)} viagens)\n"
                f"Taxa de Cancelamento: {cancellation_rate:.2f}% ({len(cancelled)} viagens)\n"
                f"Cancelamentos de Clientes: {customer_cancel_rate:.2f}% ({len(customer_cancelled)} viagens)\n"
                f"Cancelamentos de Motoristas: {driver_cancel_rate:.2f}% ({len(driver_cancelled)} viagens)\n"
                f"{'='*30}"
            )
            
            self.logger.info(stats)
            print(stats)

        except Exception as e:
            self.logger.error(f"Erro ao analisar dados: {e}")
