export type SDKConfig = {
  baseUrl: string;
  apiKey?: string;
};

export class QuantisClient {
  constructor(private config: SDKConfig) {}

  health(): object {
    return { status: "ok", baseUrl: this.config.baseUrl };
  }
}
