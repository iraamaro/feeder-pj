# feeder-pj

[![GitHub issues](https://img.shields.io/github/issues/iramaro/feeder-pj?logo=issues&style=flat-square)](https://github.com/iramaro/feeder-pj/issues)
[![GitHub forks](https://img.shields.io/github/forks/iramaro/feeder-pj?logo=forks&style=flat-square)](https://github.com/iramaro/feeder-pj/network)
[![GitHub stars](https://img.shields.io/github/stars/iramaro/feeder-pj?color=yellow&logo=stars&style=flat-square)](https://github.com/iramaro/feeder-pj/stargazers)
[![GitHub license](https://img.shields.io/github/license/iramaro/feeder-pj?logo=license&style=flat-square)](https://github.com/iramaro/feeder-pj/blob/master/LICENSE)
[![Telegram](https://img.shields.io/badge/telegram-%40iramaro-9cf)](https://t.me/iramaro)&nbsp;

> A simple query for enterprises names.
> The query used in [ReceitaWS](https://receitaws.com.br/api)
> Persistence with projects like [socios-brasil](https://github.com/turicas/socios-brasil)

## URL Base

> URL for free GET: https://www.receitaws.com.br/v1/cnpj/ + ```[cnpj]```

**GET: 3 requests per minute.**

[https://www.receitaws.com.br/v1/cnpj/](https://www.receitaws.com.br/v1/cnpj/)

## Install

Make sure you are running a python 3 runtime.

```bash
git clone https://github.com/iramaro/feeder-pj.git
pip install -r requirements.txt
```
## Examples

Use the cnpjs.xlsx file for test. Hold in the first column the CNPJs.

| cnpj           | razao-social                                                  |
|----------------|---------------------------------------------------------------|
| 15141799000103 | CIA DE FERRO LIGAS DA BAHIA FERBASA                           |
| 02998611000104 | CTEEP - COMPANHIA DE TRANSMISSAO DE ENERGIA ELETRICA PAULISTA |
| 60872504000123 | ITAU UNIBANCO HOLDING S.A.                                    |
| Erro           |                                                               |
| 60894730000105 | USINAS SIDERURGICAS DE MINAS GERAIS S/A. USIMINAS             |
| Erro           |                                                               |
| 60840055000131 | FLEURY S.A.                                                   |

## WARNING

THIS IS AN EXPERIMENTAL SOFTWARE. **USED IN A SPECIFIC STUDY. DO NOT USE LIKE OFFICAL PROJECTS (LEGAL EVIDENCE OR RISK MANAGEMENT)!**

